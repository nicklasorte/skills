---
name: "matlab-builtin-first"
description: "Use for every request that produces or changes MATLAB code, even when the word MATLAB isn't used — \"write a function,\" \"read this file,\" \"convert this,\" \"plot,\" \"loop over,\" \"make a KML,\" \"fix this .m file,\" \"why does this error,\" or any task in spectrum, geospatial, Census, or Monte Carlo pipelines. Finds the built-in MATLAB or toolbox function for each step, verifies it in the live MATLAB session, and lints and runs the code before delivery, instead of writing the logic from scratch. For tracing an entry point into a methodology report, use matlab2paper."
---

# MATLAB built-in first

These rules assume MATLAB R2025b; adjust function names for the user's release. For each step of a task, use the built-in MATLAB or toolbox function that does it. Write custom logic only for the part that no built-in covers. The code doesn't need to run in Octave, so never avoid a toolbox function for compatibility and never add Octave caveats.

Check which toolboxes are installed before you choose a function: run `detect_matlab_toolboxes` once per session and treat the result as the list of what's available.

If the Optimization Toolbox or Global Optimization Toolbox is missing, `fmincon`, `linprog`, `optimoptions`, and `ga` fail with a license error even though `which` finds some of them in a shared library. In that case, use the base-MATLAB `fminsearch`, `fminbnd`, or `fzero`, or ask the user. The same check applies to Image Processing, Control System, and Curve Fitting. `which` alone doesn't prove a function is licensed.

## Why

Hand-rolled code is the most common thing users correct. Typical replacements are `regexp` KML parsing with `readgeotable`, a custom equal-area centroid with `polyshape` and `centroid`, `fprintf` KML with `kmlwrite`, manual trigonometry with `track1`, shell-out `git clone` with `gitrepo`, loops with `ismember` and `strjoin`. Each correction cost a round trip and came with a documentation link. The built-in is tested by MathWorks, handles edge cases the user hasn't mentioned, and matches what the user reads in the docs.

A second failure is remembered syntax. `kmlwrite` was once delivered with unverified name-value arguments. The live MATLAB session makes that unnecessary.

A third failure is code that passes serially and breaks in production. Simulations often run on a parallel pool and with several compiled servers working the same folder at once, picking folders in random order and sharing cache files. A `parfor` loop that indexes a function handle, or a `save` that another server reads half-written, only shows up there. Test both before delivery (step 5).

## Workflow

### 1. Decompose

Split the request into steps: read, clean, compute, geometry, output. Name the candidate built-in for each step before you write anything. Use `references/function-map.md` for the task-to-function map in the user's domains, and open it whenever a step touches files, geography, Census data, sets, interpolation, statistics, randomness, numerical methods, signal processing, or large data.

### 2. Verify in MATLAB, not from memory

The MATLAB MCP server tools are available in chat and in Claude Code (`detect_matlab_toolboxes`, `check_matlab_code`, `evaluate_matlab_code`, `run_matlab_file`, `run_matlab_test_file`). Load them with ToolSearch if they are deferred. Then probe:

```matlab
which -all kmlwrite          % confirms the function exists and which toolbox owns it
help kmlwrite                % exact signature and name-value arguments for this release
lookfor centroid             % finds candidate built-ins when you don't know the name
```

Write every call from `help` output, not from recall. If `which` returns nothing, the function doesn't exist in this release. Find another name before falling back to custom code.

Read the "See also" line at the bottom of `help` output. It often names a more specific built-in that fits better, for example `kmlwritepoint` instead of the general `kmlwrite` for named points.

Probe the simplest call before writing a helper. For example, `string(c)` converts a mixed cell of text, integers, and logicals in one call, so a `cellfun` helper is unnecessary.

When the session isn't reachable, search the web for the function and fetch its MathWorks reference page (`mathworks.com/help/<product>/ref/<function>.html`). Say in one line that the syntax came from the docs, not from a run.

### 3. Use MATLAB Answers to find names, not to copy code

When you don't know whether a built-in exists for a step, search MATLAB Answers (`mathworks.com/matlabcentral/answers`) with the task phrased as a question, for example "write polygon to KML". Read the thread for function names, then verify each with `which` and `help`.

Rank replies this way: a MathWorks Staff or MathWorks Support Team reply, then the most recent reply, then the accepted answer. Accepted answers are often a decade old and point to File Exchange packages that a later built-in replaced. Don't recommend File Exchange submissions when an installed toolbox covers the task.

### 4. Write

- Version-suffix the file name: `_rev1`, `_rev2`.
- Use `arguments` blocks for input validation instead of manual `nargin` and `isa` checks.
- Fail loudly with `error()` and an identifier. Don't use `pause`, a silent `break`, or skipped rows.
- Don't invent constants. Cite the source or mark the value `TODO`.
- For each custom block, add a one-line comment naming the built-ins you considered and why they don't fit, so the user can overrule you.
- Make surgical edits to existing code. Don't rewrite a working function to swap in built-ins unless the user asks.
- Match the surrounding code's naming and style (for example, `snake_case` variables versus camelCase) instead of imposing your own.
- Preallocate before a loop (`zeros`, `NaN`, `cell`); never grow an array inside one.
- Keep full precision in computed values. Round only for display, never with `round(x, n)` inside a calculation.
- When the code goes into a compiled app or onto a server that may lack toolboxes, list the products it needs with `matlab.codetools.requiredFilesAndProducts`.
- Bound every retry. A `while(retry==1)` loop around `load`, `save`, or `cd` hangs an unattended server forever; use a `for` loop with a try count and then `error()`.
- Inside `parfor`, call a function handle with `feval(fcn, args)`; indexing it (`fcn(args)`) is rejected as a sliced variable. Random draws inside `parfor` come from a `RandStream` with one substream per iteration, never `rng(seed+k)`.
- Files that another process may read while they are written (cache chunks, result files, status files in a shared Rev folder) are written to a uniquely named temporary file in the same folder and renamed into place with `java.nio.file.Files.move(src, dst, [REPLACE_EXISTING, ATOMIC_MOVE])`. MATLAB's `movefile` is not atomic: on R2025b a reader saw the destination missing 45 times and unreadable 3 times during 300 replacements; the Java move saw 0 and 0. Use first-writer-wins (keep the existing file, discard the temp) for cache chunks that any server may produce. `save_mat_retry_rev1` in Basic_Functions does this.
- When several servers share a folder, a server that finishes a result must not break one still working: before using its own stitched chunks, a server checks whether the result files now exist and loads those instead; a chunk file that vanished between its parallel pass and its serial pass is recomputed or replaced by the finished result, never treated as data.

### 5. Lint and run before delivery

1. `check_matlab_code` and `run_matlab_file` need a file on the user's computer. Write it to `fullfile(tempdir, "<task>")` with `evaluate_matlab_code`; for multi-line files, pass the content base64-encoded and decode it with `matlab.net.base64decode`, which avoids quote escaping. When a connected folder is available, write there with the device tools instead; hand-copied base64 over a few kilobytes gets corrupted.
1. Run `check_matlab_code` on the file. Fix every message or justify it with `%#ok<ID>` and a reason.
1. Run the function once with `evaluate_matlab_code` or `run_matlab_file`. Use a small synthetic input you construct, or the file the user named when they attached it or gave a path. Report the actual output values in one line.
1. If the run fails, fix and rerun. Don't deliver code that hasn't executed.
1. **Parallel check.** Whenever the code has a `parfor`, takes a `parallel_flag`, or is called from one, run it with `parallel_flag=1` on a real pool (`gcp` or `parpool(2)`) and confirm the result equals the `parallel_flag=0` run for the same seed. Add the workers' paths with `parfevalOnAll(@addpath, 0, folder)` first.
1. **Multi-server check.** Whenever the code reads or writes a shared Rev folder (chunk caches, result files, checkout or status files, `persistent_var_exist_*`, `persistent_delete_*`), simulate two servers: launch the same call twice with `parfeval` on two workers, same folder, different `rng` seeds, and confirm both return without error, the result files are complete and loadable, no `sub_*` chunk or `*.part.mat` temp files remain, and a reader polling the file during the writes never sees a partial or missing file. Put these in the test file (see `references/testing.md`) and filter them with `assumeTrue` when no pool exists, so they are reported as filtered, not passed.

Don't deliver until all pass, and don't describe this process in the reply; report the result.

For new reusable functions, write tests as `references/testing.md` describes, including the parallel and multi-server tests above whenever they apply.

## Choosing between built-ins

Some built-ins have known pitfalls:

| Avoid | Use | Why |
| --- | --- | --- |
| `num2str` or `string` on non-integers | `compose("%.15g", v)` or `sprintf` | Both round non-integers (`num2str(3.14159265)` is `'3.1416'`; `string(123456.789012345)` is `"123456.789"`). Both are exact for integers up to `flintmax`. Verified in R2025b. |
| `readtable` on mixed columns | `readcell` | `readtable` silently converts unparseable text, such as values with non-breaking spaces, to `NaN`. |
| `str2num` | `str2double` | `str2num` returns `[]` on bad input and evaluates arbitrary code. |
| `interp1(...,'spline')` | `interp1(...,'linear')` or `griddedInterpolant` | Spline overshoots on non-monotone data. |
| `rand` with `rng` inside `parfor`, or `rng(seed+k)` per iteration | `RandStream('mrg32k3a')` with `Substream=k` | Reproducibility across workers, and independence: `rng(seed+k)`, `rng(seed+k+1)`, `rng(seed+k+2)` for three variables makes variable 2 at iteration k identical to variable 1 at iteration k+1. Verified in R2025b. |
| `movefile` for a file another process reads | `java.nio.file.Files.move` with `ATOMIC_MOVE` | `movefile` deletes and copies; readers see a missing or partial file. Verified in R2025b. |
| `prctile(x, p)` with few draws in the tail | more draws, or report the sample maximum | With n draws, `prctile` returns the sample maximum once n*(100-p)/100 < 1; 1000 draws at the 99.97th percentile is one extreme value. Verified in R2025b. |
| `strcat` on char | `[a b]`, `strjoin`, or `join` | `strcat` strips trailing whitespace from char arrays. |
| `a == b` or `abs(a-b) < eps` on computed values | `ismembertol`, `uniquetol`, or `abs(a-b) <= tol*max(abs(a),abs(b))` | `eps` is absolute and tiny: `1000.1 + 0.2` vs `1000.3` fails both `==` and the `eps` test but passes `ismembertol`. Verified in R2025b. Exact `==` is fine on integers and stored codes. |
| `arrayfun` or `cellfun` to speed up numeric work | Vectorized operations, or a preallocated loop | For 1e6 elements: `arrayfun` 0.63 s, preallocated loop 0.0095 s, vectorized 0.0011 s. Verified in R2025b. `cellfun` stays the right tool for per-element type checks on mixed cells. |
| `inv(A)*b` | `A\b` (or `decomposition` for repeated solves) | On `hilb(8)`, the residual is 1.4e-07 with `inv` and 4.6e-16 with `\`. Verified in R2025b. |
| `bsxfun` | Implicit expansion (`M - v`) | Identical results, verified in R2025b; implicit expansion has made `bsxfun` unnecessary since R2016b. |

## When speed matters

Only when the user asks for speed, or the code will run over large data. Don't rewrite working code for speed unasked.

1. Measure first: `timeit` for one function, `profile on` / `profile viewer` for a pipeline. Fix the line the profiler names, not the one that looks slow.
1. Vectorize with implicit expansion and logical indexing; keep a preallocated loop when vectorizing would hurt clarity or memory.
1. For data that doesn't fit in memory: `matfile` for partial loads of a `.mat` file, `tall` arrays for out-of-memory tables, `sparse` for mostly-zero matrices.
1. For parallel Monte Carlo, `parfor` with `RandStream` substreams; `gpuArray` only for large dense array math, and check the speedup with `timeit` and `gather`.

## Reply format

Lead with the file. Then at most three lines: what the function does, the run result (including the parallel and multi-server results when they ran), and any built-in you chose over an alternative. No preamble.