# Code, placeholders, and UI elements

Paraphrased from the Google developer documentation style guide (CC BY 4.0): Code in text, Placeholders, Command-line syntax, UI elements.

## Code font in prose

Use code font (backticks in Markdown) for anything the reader types verbatim or that names a code entity:

- Attribute, parameter, field, and property names and values
- Class, method, and function names; language keywords; data types; enums; constants
- Filenames, extensions, paths, and directories
- Command-line tools and commands (`gcloud`, `kubectl`, `curl`)
- Environment variables, package names, namespaces
- Database tables, rows, columns
- HTTP verbs (`POST`), status codes (`404 Not Found`), content-type values
- IP addresses, port numbers, query parameters
- Strings and URLs used inside code or commands
- Text the reader enters in a field
- Placeholders

**Not** code font: product, service, and organization names; domain names in ordinary prose; URLs the reader visits in a browser (better: a descriptive link).

**Sometimes**
- Boolean values in code font when they're literal values (`true`); plain when describing a condition ("if true…").
- Tool vs. project: `curl` the command, curl the project.
- Email addresses: code font if typed as input; plain linked text if it's a contact.

Don't wrap code in quotation marks unless the quotes are part of the code.

## Grammar with code elements

- Don't use code elements as verbs or inflect them. Add a noun and inflect the noun.
  - "Send a `POST` request," not "`POST` the data."
  - "The `ADDRESS` constant's value," not "`ADDRESS`'s value."
  - "`INT64` values," not "`INT64`s."
- Method names: drop the class prefix unless needed to disambiguate ("call its `get` method").
- HTTP status codes: "an HTTP `400 Bad Request` status code" (status code, not response or error code). Ranges: "`2xx`," or "in the `200`-`299` range."

## Command-line syntax and code samples

- Introduce a command by what it does, not "Run the following command": "Create the bucket:".
- Show output with "The output is similar to the following:" in its own code block.
- Optional arguments in square brackets, mutually exclusive choices in braces with pipes, repeatable arguments with an ellipsis. Don't put these symbols inside placeholder markup.
- Commands the reader copies shouldn't contain `[ ]`, `{ }`, `|`, or `...`; give separate commands for the variants instead.
- Keep input and output in separate code blocks. Don't show a shell prompt with the current directory.
- Show omitted output lines as `...` (three periods) on their own line, never the ellipsis character (…).

## Placeholders

- Name: uppercase with underscores, descriptive: `PROJECT_ID`, `INSTANCE_NAME`. Not `my_project`, `YOUR_NAME`, `foo`, `x`, `xxx` (except conventional forms like `4xx`).
- Markup: Markdown inline `*`PLACEHOLDER`*`; HTML `<code><var>PLACEHOLDER</var></code>`.
- Explain every placeholder at first use, right after the code block:
  - One: "Replace `BUILD_ID` with the ID of the build that you copied earlier."
  - Several: "Replace the following:" then a bulleted list in the order the placeholders appear, each `` `NAME` ``: lowercase description, with examples introduced by an em dash or "such as."
- Placeholders in output: follow with "This output includes the following values:" and the same list format.

## UI elements

- Bold the UI element's exact label: Click **Save**. Match the UI's capitalization.
- UI element that shows code-like or user-entered text (instance names): bold plus code font: **`my-instance`**.
- Verbs: *click* (not "click on") for desktop; *tap* on mobile; *select* for checkboxes and list choices; *clear* to uncheck a checkbox (not *uncheck*); *deselect* for other UI elements; *enter* for text (prefer it to *type*, because there's usually more than one way to enter text); *press* for keys and physical buttons; *point to* or *hold the pointer over* (not *hover*); *drag* (not "click and drag").
- Prepositions: *in* a dialog, field, list, menu, pane, or window; *on* a page, tab, or toolbar.
- Don't use a UI label as a verb: "In the **Name** field, enter a name," not "**Name** the account."
- Call a menu item a *command*, not an *option* or *choice*.
- If a UI label is in all caps, write it in sentence case.
- Hyphenate *right-click*, *double-click*. *Checkbox* is one word.
- Menu paths with `>`: **File > New > Document**.
- Say where before what: "In the **Network** list, select **`my-net-2`**."
- Don't name elements by position or appearance ("the button on the right," "the three-line icon"); use the element's label or accessible name (**Menu**). Add a screenshot if it's hard to find.
- Say *dialog*, not *dialog box* or *pop-up*; *list* or *menu*, not *drop-down* unless needed.
- *Unavailable*, not *grayed out*.

## Keyboard keys

- Format combinations with plus signs and no spaces: `Control+C`.
- Spell out modifier names (*Control*, *Command*, *Option*, *Shift*, *Alt*); don't use symbols.
- Use uppercase for letter keys (`Control+S`, not `Control+s`).
- When the audience includes macOS, give the macOS shortcut in parentheses: `Control+C` (`Command+C` on macOS).
- Write "the Esc key" where the key name alone could be ambiguous.
- In procedures, prefer describing the action over giving the shortcut.
