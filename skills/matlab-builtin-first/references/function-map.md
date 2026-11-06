# Task-to-function map

Candidate built-ins for the steps that recur in spectrum, geospatial, and simulation work. Verify each one with `which -all` and `help` before use; names and arguments change between releases. Organized by the MathWorks documentation categories.

## Contents

- [Data import and export](#data-import-and-export)
- [Strings and mixed cells](#strings-and-mixed-cells)
- [Sets, grouping, and lookup](#sets-grouping-and-lookup)
- [Geography (Mapping Toolbox)](#geography-mapping-toolbox)
- [Geometry](#geometry)
- [Interpolation and statistics](#interpolation-and-statistics)
- [Randomness and Monte Carlo](#randomness-and-monte-carlo)
- [RF and signal units](#rf-and-signal-units)
- [Parallel and caching](#parallel-and-caching)
- [Source control and files](#source-control-and-files)
- [Numerical methods](#numerical-methods)
- [Signal processing](#signal-processing)
- [Large data](#large-data)
- [Validation and testing](#validation-and-testing)

## Data import and export

| Task | Built-in | Note |
| --- | --- | --- |
| Read spreadsheet with mixed numeric and text | `readcell` | Preserves raw text; `readtable` turns bad cells into `NaN`. |
| Read clean tabular data | `readtable`, `detectImportOptions` | Set `VariableNamingRule="preserve"` to keep headers. |
| Write tables and cells | `writetable`, `writecell`, `writematrix` | One call per sheet with `Sheet=`. |
| Read and write JSON | `jsondecode`, `jsonencode`, `readstruct`, `writestruct` | |
| Read XML or KML as a struct | `readstruct` | For KML geometry use `readgeotable` instead. |
| Read fixed-width or delimited text | `readmatrix`, `textscan` | |
| Read a URL | `webread`, `websave` | `weboptions` for timeouts and headers. |
| Save and load MAT | `save`, `load`, `matfile` | `matfile` for partial loads of large files. |

## Strings and mixed cells

| Task | Built-in | Note |
| --- | --- | --- |
| Number to text | `string`, `compose`, `sprintf` | `string` and `num2str` are exact for integers up to `flintmax` but round non-integers; use `compose("%.15g", v)` for those. |
| Mixed cell to text | `string(c)`, then `cellstr` if char is needed | Handles text, integer, and logical elements in one call. |
| Text to number | `str2double` | Returns `NaN`, never `[]`. |
| Strip Unicode whitespace | `strtrim`, `regexprep(s, '[\s\x{00A0}\x{202F}]', '')` | `\s` alone misses non-breaking spaces. |
| Join and split | `strjoin`, `join`, `split`, `strsplit` | |
| Convert mixed cell to char | `cellfun(@class, c, UniformOutput=false)`, `cellfun(@ischar, c)` | Branch with `cellfun`, not a loop. |
| Pattern matching | `contains`, `startsWith`, `extract`, `pattern` | `pattern` objects replace most `regexp`. |

## Sets, grouping, and lookup

| Task | Built-in | Note |
| --- | --- | --- |
| Index match between arrays | `ismember` | Second output gives the location. |
| Set difference, union, intersection | `setdiff`, `union`, `intersect` | `'stable'` keeps input order. |
| Unique with counts | `unique`, `groupcounts`, `histcounts` | |
| Aggregate by group | `groupsummary`, `accumarray`, `splitapply`, `findgroups` | `groupsummary` for tables, `accumarray` for index vectors. |
| Nearest neighbor | `knnsearch`, `dsearchn`, `rangesearch` | `knnsearch` is Statistics and Machine Learning Toolbox. |
| Sort with index | `sort`, `sortrows`, `maxk`, `mink` | |

## Geography (Mapping Toolbox)

| Task | Built-in | Note |
| --- | --- | --- |
| Reference ellipsoid | `wgs84Ellipsoid("km")` | Pick the length unit here once. |
| Geodesic distance and azimuth | `distance(lat1,lon1,lat2,lon2,ellipsoid)` | Returns arc length in ellipsoid units. |
| Point from start, azimuth, range | `reckon` | |
| Evenly spaced track | `track1`, `track2` | `'rh'` for rhumb line, `'gc'` for great circle. |
| Circle on the sphere | `scircle1`, `scircle2` | For coordination-zone rings. |
| Read shapefile, KML, GeoJSON | `readgeotable`, `geotable2table`, `shaperead` | |
| Write KML | `kmlwrite`, `kmlwritepoint`, `kmlwriteline`, `kmlwritepolygon` | Pass a geotable or lat/lon vectors. |
| Point in polygon | `inpolygon`, `isinterior` (polyshape) | Use projected or small-extent coordinates. |
| Geographic axes plotting | `geoplot`, `geoscatter`, `geobasemap` | |
| Projection | `projfwd`, `projinv`, `projcrs`, `geocrs` | |
| Area of a geographic polygon | `areaint` | On the ellipsoid; `polyarea` is planar. |

## Geometry

| Task | Built-in | Note |
| --- | --- | --- |
| Polygon object | `polyshape` | Methods: `centroid`, `area`, `boundary`, `isinterior`, `intersect`, `union`, `subtract`, `polybuffer`. |
| Convex hull | `convhull`, `boundary` | |
| Triangulation | `delaunay`, `delaunayTriangulation` | |
| Angle wrap | `wrapTo180`, `wrapTo360`, `wrapToPi` | Mapping Toolbox. |
| Vector norms and dot products | `vecnorm`, `dot`, `cross` | |

## Interpolation and statistics

| Task | Built-in | Note |
| --- | --- | --- |
| 1-D interpolation | `interp1`, `griddedInterpolant` | Default `'linear'`; avoid `'spline'` on non-monotone rows. |
| Gridded 2-D and N-D | `interp2`, `interpn`, `griddedInterpolant` | |
| Scattered | `scatteredInterpolant`, `griddata` | |
| Percentiles and quantiles | `prctile`, `quantile` | Base MATLAB since R2025b (verified). `Method="exact"` or `"approximate"`. |
| Empirical CDF | `ecdf`, `histcounts(...,Normalization="cdf")` | |
| Fit distribution | `fitdist`, `makedist` | `makedist("Normal",mu=,sigma=)` then `icdf`. |
| Gaussian quantile | `norminv`, `icdf` | |
| Running stats | `movmean`, `movmax`, `cummax`, `cumsum` | |
| Regression | `fitlm`, `polyfit`, `regress` | |
| Root finding and optimization | `fzero`, `fminbnd`, `fminsearch`, `fmincon` | |

## Randomness and Monte Carlo

| Task | Built-in | Note |
| --- | --- | --- |
| Seeded generator | `rng(seed)`, `RandStream` | `RandStream("Threefry",Seed=)` supports substreams. |
| Independent streams per worker | `RandStream.create(...,NumStreams=,StreamIndices=)` | Avoid correlated draws in `parfor`. |
| Uniform, normal | `rand`, `randn`, `random` | |
| Weighted sampling | `randsample(n,k,true,w)`, `datasample` | Statistics and Machine Learning Toolbox. |
| Draw from arbitrary CDF | `interp1(cdf, x, rand(n,1))` | Monotone `cdf` required; dedupe with `unique(...,'last')`. |

## RF and signal units

| Task | Built-in | Note |
| --- | --- | --- |
| dB conversions | `db2pow`, `pow2db`, `db2mag`, `mag2db` | Signal Processing Toolbox. |
| Aggregate powers in dBm | `pow2db(sum(db2pow(p_dBm)))` | Sum in linear, convert back. |
| Free-space path loss | `fspl` | Phased Array System Toolbox. |
| Antenna patterns | `phased.CustomAntennaElement`, `pattern` | |
| Propagation models | `propagationModel`, `pathloss`, `rxsite`, `txsite` | Antenna Toolbox and Communications Toolbox. |
| Convolution of distributions | `conv` on PDFs, or combine Gaussians analytically | Variances add; see learnings. |

## Parallel and caching

| Task | Built-in | Note |
| --- | --- | --- |
| Parallel loop | `parfor`, `parpool`, `parfeval` | |
| Hash a cache key | `keyHash`, `matlab.lang.makeValidName` | `keyHash` since R2024a. |
| File lock across servers | `matlab.io.datastore` patterns or `fopen` with exclusive write | No native lock; document the protocol. |
| Progress | `parforWaitbar`, `DataQueue` | |

## Source control and files

| Task | Built-in | Note |
| --- | --- | --- |
| Clone and pull | `gitclone`, `gitrepo`, `pull`, `fetch`, `status` | Native since R2023b. |
| Path management | `addpath(genpath(d))`, `rmpath` | Don't `savepath` for temp clones. |
| Paths and names | `fullfile`, `fileparts`, `dir`, `isfolder`, `mkdir` | |
| Secrets | `getSecret`, `setSecret` | Keep tokens out of `.m` files. |
| Temp files | `tempname`, `tempdir` | |

## Numerical methods

| Task | Built-in | Note |
| --- | --- | --- |
| Linear solve | `A\b`, `decomposition`, `lsqminnorm` | Never `inv(A)*b`. `decomposition` reuses a factorization across solves. |
| Conditioning check | `cond`, `rcond` | Check before trusting a solve on near-singular data. |
| Eigen and singular values | `eig`, `eigs`, `svd`, `svds` | `eigs`/`svds` for a few values of a large sparse matrix. |
| ODEs | `ode45` (nonstiff), `ode15s` (stiff), `odeset` | Set `RelTol` and `AbsTol` explicitly. |
| Integration | `integral`, `trapz`, `cumtrapz` | `trapz` for sampled data. |
| Minimum, no toolbox | `fminsearch` (multivariable), `fminbnd` (one variable on an interval), `fzero` (root) | Base MATLAB; these need no extra toolbox. |
| Constrained minimum | `fmincon`, `linprog`, `intlinprog`, `quadprog`, `lsqnonlin`, `fminunc` | Optimization Toolbox, which may not be installed: they fail with a license error when it's missing. Use `fminsearch` with a penalty or bound transform, or ask the user. |
| Global search | `ga`, `particleswarm`, `GlobalSearch`, `MultiStart` | Global Optimization Toolbox, **not installed**. |
| Float comparison | `ismembertol`, `uniquetol` | Not `==` or `eps` on computed values. |

## Signal processing

| Task | Built-in | Note |
| --- | --- | --- |
| Spectrum | `fft`, `ifft`, `fftshift`, `nextpow2` | Scale by length and fold for a one-sided spectrum. |
| Power spectral density | `pwelch`, `periodogram` | Signal Processing Toolbox. |
| Time-frequency | `spectrogram`, `stft` | |
| Filter design | `designfilt`, `fir1`, `butter` | `designfilt` returns a `digitalFilter` object. |
| Zero-phase filtering | `filtfilt` | `filter` adds phase delay. |
| Convolution | `conv`, `conv2`, `fftfilt` | `fftfilt` for long signals. |
| Resampling | `resample`, `interp1` | |

## Large data

| Task | Built-in | Note |
| --- | --- | --- |
| Partial load of a large `.mat` | `matfile` | Requires `-v7.3` files for partial writes. |
| Out-of-memory tables | `tall`, `datastore`, `gather` | Operations are deferred until `gather`. |
| Mostly-zero matrices | `sparse`, `nnz`, `spalloc` | |
| GPU math | `gpuArray`, `gather` | Parallel Computing Toolbox; measure with `timeit`. |
| Profiling | `profile`, `timeit`, `tic`/`toc` | `timeit` for one function; `profile` for a pipeline. |

## Validation and testing

| Task | Built-in | Note |
| --- | --- | --- |
| Input validation | `arguments` block, `mustBeNumeric`, `mustBePositive`, `validateattributes` | |
| Lint | `checkcode` (via `check_matlab_code`) | |
| Unit tests | `matlab.unittest`, `runtests`, `assert` | `run_matlab_test_file` runs them. |
| Timing | `timeit`, `tic`/`toc` | |
| Dependencies | `matlab.codetools.requiredFilesAndProducts` | Lists toolboxes a file needs. |
