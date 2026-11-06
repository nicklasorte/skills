# Writing tests

Follows the MathWorks unit testing framework guidance and `matlab.unittest` conventions, adapted to Nick's repos. Every pattern here was run in R2025b.

## Contents

- [When to write tests](#when-to-write-tests)
- [File convention](#file-convention)
- [What to test](#what-to-test)
- [Mechanics](#mechanics)
- [Check that the tests can fail](#check-that-the-tests-can-fail)
- [Run and report](#run-and-report)
- [Template](#template)

## When to write tests

- **New reusable function:** write a test file with it. Skip tests for one-off scripts, plots, and `init_*` entry scripts, which configure a study rather than compute something reusable.
- **Bug fix:** first write a test that reproduces the bug and watch it fail, then fix the code and watch it pass. The test stays as a regression guard.
- **Edit to a function that has tests:** run them before and after the edit.
- **New `_revN` of a function:** copy its test file to the new revision and rename the class, so the old revision's tests stay valid for the old file.

## File convention

Follow the repo's existing convention first:

- **`imt-matlab`** uses self-test functions named `test_<function>.m` that return results, run by `run_all_tests.m`. Write new tests in that style and add the new file to the list in `run_all_tests.m`.
- **Elsewhere** (`General_Movelist`, `Basic_Functions`, and new repos), use a class-based test, `classdef test_<function_name> < matlab.unittest.TestCase`, in a file named `test_<function_name>.m`, beside the function or in the repo's `tests/` folder if it has one.

`runtests` and `testsuite` find any file whose name starts or ends with `test`, so the `test_` prefix matches Nick's snake_case and is discovered without configuration. MathWorks' examples use a `Test.m` suffix; either works.

Class-based tests are the default because they add parameterized tests, fixtures, and tags. Use function-based tests (`functiontests(localfunctions)`) only for a trivial function, and script-based tests never.

## What to test

Aim for 4 to 10 tests per function, chosen from these categories. Each test checks one behavior and is named for it (`latitudeConstant`, `invalidLatitudeErrors`).

1. **Known value from an independent source.** A hand calculation, a worked example from the recommendation the function implements (ITU-R recommendations often include test values), or a different built-in. Never compute the expected value with the function under test or a copy of its logic. For example, check `track1` spacing with `distance`, not with `track1`.
1. **Invariants and physics.** Properties that must hold for any valid input: a linear power sum is at least its largest term; two equal powers sum to +3.01 dB; free-space path loss rises 6.02 dB per doubling of distance; percentiles don't decrease as p increases; a due-east rhumb line holds latitude constant.
1. **Edge cases.** Empty input, scalar versus vector, `NaN` handling, boundaries (latitude ±90, longitude ±180 and the antimeridian, zero distance, a single Monte Carlo draw).
1. **Error paths.** One `verifyError` per validation, with the identifier: `arguments`-block validators raise `MATLAB:validators:*` (for example `MATLAB:validators:mustBeInRange`), and custom checks raise the identifier the function passes to `error`.
1. **Reproducibility, for stochastic code.** The same seed gives identical output; different seeds give different output; draws meant to be independent are uncorrelated. A test that iteration k's EIRP draw differs from iteration k+1's path-loss draw would have caught the seed overlap in `vector_mc_seed_pr_eirp_clutter_rev1`.
1. **Output contract.** `verifySize` and `verifyClass` on each output, so a downstream caller that indexes the result doesn't break silently.

## Mechanics

- **Tolerances.** Compare doubles with `verifyEqual(actual, expected, "AbsTol", tol)` or `"RelTol", tol`. Choose the tolerance from the physics, not from `eps`: about 1e-9 relative for geometry, 0.01 dB for dB quantities, and a statistical bound (several standard errors) for Monte Carlo estimates.
- **verify, not assert.** `verify*` records a failure and keeps testing; `assert*` stops the test. Use `assume*` to skip a test whose prerequisite is missing, for example `testCase.assumeNotEmpty(which("tirempl"))`.
- **Parameterize across conditions.** Put conditions in `properties (TestParameter)` as a struct of named cases. One convenient case can hide a bug: a great-circle track passed the equator case of the due-east test, because at the equator a great circle and a rhumb line due east coincide, while the 38.9° and 70° cases failed.
- **Independence.** Tests run in any order and share nothing. Write files only inside `matlab.unittest.fixtures.TemporaryFolderFixture`, change the path only with `PathFixture`, and never read or write a study's revision folder or cache files.
- **Speed.** Use tiny inputs: a few base stations, `mc_size` of about 100 with a fixed seed. Tag anything over a few seconds with `TestTags = {'Slow'}` so it can be excluded.

## Check that the tests can fail

A passing test only counts if it would fail on wrong code. After the tests pass:

1. Copy the function to a temporary folder and plant one plausible bug, such as `"gc"` for `"rh"`, `+` for `-`, an off-by-one index, or `10*log10` for `20*log10`.
1. Copy the test file into the same folder, `cd` there, and run it. MATLAB's current folder outranks the path, so running from the original folder silently tests the original file.
1. Confirm at least one test fails, then delete the temporary folder.

If no test fails, add one that would.

## Run and report

Run the test with the `run_matlab_test_file` tool, or with `runtests('test_<function_name>')`. For a coverage report, use `runtests('test_<function_name>', 'ReportCoverageFor', '<function>.m')`, which writes an HTML report.

Report in one line: tests passed, and how many failed against the planted bug. For example: "10 tests pass; 4 fail against a planted great-circle bug."

## Template

Verified in R2025b: 10 tests pass on `east_track_rev1`, and 4 fail when `track1("rh", ...)` is changed to `track1("gc", ...)`.

```matlab
classdef test_east_track_rev1 < matlab.unittest.TestCase
    %TEST_EAST_TRACK_REV1 Unit tests for east_track_rev1.
    %   Run with: runtests('test_east_track_rev1')

    properties (TestParameter)
        % Latitudes that exercise the equator, mid-latitude, and high latitude.
        lat0 = struct('equator', 0, 'dc', 38.9, 'high', 70)
    end

    properties (Constant)
        Ellipsoid = wgs84Ellipsoid("m")
    end

    methods (Test)
        function firstPointIsStart(testCase)
            % Known value: the track starts on the input point.
            [lat, lon] = east_track_rev1(38.9, -77.0, 1000, 11);
            testCase.verifyEqual([lat(1) lon(1)], [38.9 -77.0], "AbsTol", 1e-12);
        end

        function outputShape(testCase)
            [lat, lon] = east_track_rev1(38.9, -77.0, 1000, 11);
            testCase.verifySize(lat, [11 1]);
            testCase.verifySize(lon, [11 1]);
        end

        function latitudeConstant(testCase, lat0)
            % Invariant: a due-east rhumb line holds latitude constant.
            lat = east_track_rev1(lat0, 10, 5000, 21);
            testCase.verifyEqual(lat, repmat(lat0, 21, 1), "AbsTol", 1e-9);
        end

        function spacingEqualsStep(testCase, lat0)
            % Independent check: measure spacing with distance(), not track1.
            [lat, lon] = east_track_rev1(lat0, 10, 5000, 21);
            step = distance("rh", lat(1:end-1), lon(1:end-1), lat(2:end), lon(2:end), testCase.Ellipsoid);
            testCase.verifyEqual(step, repmat(5000, 20, 1), "RelTol", 1e-9);
        end

        function invalidLatitudeErrors(testCase)
            % Error path: bad input fails loudly with the validator's ID.
            testCase.verifyError(@() east_track_rev1(91, 0, 1000, 5), "MATLAB:validators:mustBeInRange");
        end

        function tooFewPointsErrors(testCase)
            testCase.verifyError(@() east_track_rev1(0, 0, 1000, 1), "MATLAB:validators:mustBeGreaterThan");
        end
    end
end
```
