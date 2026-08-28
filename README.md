# Instructions to start an HSF Training module as a Jupyter Book

[![tests](https://github.com/hsf-training/cookiecutter-jupyter-book/actions/workflows/tests.yml/badge.svg)](https://github.com/hsf-training/cookiecutter-jupyter-book/actions/workflows/tests.yml)
[![pre-commit.ci status](https://results.pre-commit.ci/badge/github/hsf-training/cookiecutter-jupyter-book/main.svg)](https://results.pre-commit.ci/latest/github/hsf-training/cookiecutter-jupyter-book/main)
[![Check Markdown links](https://github.com/hsf-training/cookiecutter-jupyter-book/actions/workflows/check-links.yaml/badge.svg)](https://github.com/hsf-training/cookiecutter-jupyter-book/actions/workflows/check-links.yaml)

This repository holds the template for starting a new [HSF Training module](https://hepsoftwarefoundation.org/training/curriculum.html) as a [Jupyter Book](https://jupyterbook.org/) (see, for example, our [training on Docker and Podman](https://hsf-training.github.io/hsf-training-docker/)).
For the legacy Jekyll/carpentries style, see [carpentry-cookiecutter](https://github.com/hsf-training/carpentry-cookiecutter) instead.

## Credits

This template is adapted from the excellent [executablebooks/cookiecutter-jupyter-book](https://github.com/executablebooks/cookiecutter-jupyter-book)
by Tomas Beuzen and the [Executable Books](https://executablebooks.org/) community (BSD 3-Clause license, see [LICENSE](LICENSE)),
tailored to the conventions of [HSF Training](https://hepsoftwarefoundation.org/workinggroups/training.html).

## How to start a new module

> **Note**
> We happily do this for you! It's always best to talk to us first, if you plan to contribute to our [curriculum](https://hepsoftwarefoundation.org/training/curriculum.html).

To start a new module, install [Cookiecutter](https://github.com/cookiecutter/cookiecutter) and run

```bash
pip install -U cookiecutter
cookiecutter https://github.com/hsf-training/cookiecutter-jupyter-book/
```

Answer the questions (defaults are shown in square brackets) and you get a directory with a working
module skeleton and a `README.md`.

### Preview the website

Inside the generated directory, install the requirements and build the book:

```bash
cd /path/to/your/module
pip install -r requirements.txt
jupyter-book build book/
```

Then open `book/_build/html/index.html` in your browser.

### Additional steps

Install [`pre-commit`](https://pre-commit.com/) and install the corresponding hooks with

```bash
cd /path/to/your/module
pre-commit install
```

### Configuring your GitHub repository

After you initialized git and pushed the module to a repository in the
[hsf-training](https://github.com/hsf-training) organization, go to the repository
**Settings → Pages** and set **Source** to **GitHub Actions**.
The included workflow (`.github/workflows/deploy.yml`) then builds and deploys the book
on every push to `main`.

### Fill in content

* Pages are written in [MyST Markdown](https://jupyterbook.org/en/stable/content/myst.html); every page must be listed in `book/_toc.yml`.
* `book/01-example.md` shows the episode format (overview and key-points admonitions, exercises with dropdown solutions).
* Executable content can be added as Jupyter notebooks (see `book/notebooks.ipynb`); add any packages they need to `requirements.txt`.
* See the [Jupyter Book documentation](https://jupyterbook.org/) for everything else.

## FAQ

> This is so much to take in, I feel entirely overwhelmed and discouraged.

This is entirely normal, if you're new to the technology stack that we're using (Markdown, Jupyter Book, git, GitHub, ...). But don't despair, we're here to help you! Simply [write to us](mailto:hsf-training-wg@googlegroups.com) or [join our weekly meeting](https://indico.cern.ch/category/10294/), or join the [Mattermost educators space](https://mattermost.web.cern.ch/signup_user_complete/?id=t9zkdocffbbozqcdy193myre8y) and we'll help you get unstuck. We can also arrange a short meeting where we share screens and figure out problems.
