# attnpnts4stdnts
A structured set of attention points for students

The attention points we focus on currently are reporting-related.


## Repository structure

* The `attention_points` folder contains
  [YAML](https://en.wikipedia.org/wiki/YAML) files, each of which describes an
  _attention point_ in a structured way:

  ```yaml
  summary: >  # this must always be present
    Always write a short summary of the attention point,
    ideally worded as a commandment

  description: >  # this must always be present
    The description of the attention point. This can contain one or two
    paragraphs and should include examples if possible. URL references should go
    below.

    No convention about description markup has yet been fixed, but anything else
    than Markdown or LaTeX is unlikely to be adopted.

  references:  # this can, but should not be omitted
    - https://en.wikipedia.org/wiki/Reference
    - http://mirrors.ctan.org/info/lshort/english/lshort.pdf

  labels: [a, list, of, labels]  # at least one label must be present
  ```

  Because they function as identifiers, the _filenames should be descriptive,
  but concise_ (at most 30 characters). They should only contain alphanumeric
  ASCII characters, underscores ` `, hyphens `-`, and plusses `+`. Normal words
  should be lower case, but acronyms and the like can be uppercase.

* The `labels.yaml` file contains a structured description of all the
  (alphanumeric) _labels_ used in the attention point files. No undescribed
  label should be used. We can have a forest of labels. Namely, root labels such
  as ‘`math`’ and dependent labels (branches and leaves) such as
  ‘`math/notation`’; the slash `/` is used as a level separator.

  The actual forest of labels we will use is not yet decided. We will need to
  balance flexibility (requiring many labels) with maintainability (limiting the
  number of labels).

* The `scripts` folder contains scripts to conveniently convert the attention
  point files into documents that can be disseminated.


## Contribution

I invite and welcome pull requests to

* add well-written attention points,
* correct or improve the existing attention points,
* add scripts that provide functionality not yet present,
* correct or improve the existing scripts,
* corrections or improvements to the `README.md` files.

Obviously, in case you add labels, the file `labels.yaml` should be updated as
well.

Github's issues functionality can be used to signal issues with the scripts or
YAML files. Pull requests are preferred for issues that you can fix.


## Licenses

The content in this repository (mostly YAML and Markdown files) are licensed as
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/) and the code
(e.g., scripts to generate documents from the content) is licensed as
[GPL-3.0-or-later](https://www.gnu.org/licenses/gpl-3.0.txt).
