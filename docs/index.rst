BeeWare Theme Demo
==================

Theme checklist
---------------

Things to manually check:

Titlebar
~~~~~~~~

A dark gray titlebar is on the page. This confirms the theme template has been applied.

Site icon
~~~~~~~~~

The icon top-left has been rendered. This confirms the template can reference external
resources.

Heading font
~~~~~~~~~~~~

Headings are rendered in Cutive. This confirms the BeeWare custom CSS theme has been
applied.

Inline Code
~~~~~~~~~~~

Inline code is rendered in the same color as the surrounding font. This confirms the
CSS theme has applied.

This is text with ``inline code`` here and ``inline code`` here.

Tabbed Content Code
~~~~~~~~~~~~~~~~~~~

Code is in a contrasting color to the background. This confirms that the CSS theme has
been applied.

.. tabs::

  .. group-tab:: macOS

    .. code-block:: console

      $ git clone https://github.com/beeware/beeware-theme.git

  .. group-tab:: Linux

    .. code-block:: console

      $ git clone https://github.com/beeware/beeware-theme.git

  .. group-tab:: Windows

    .. code-block:: doscon

      C:\...>git clone https://github.com/beeware/beeware-theme.git

Table Caption Placement
~~~~~~~~~~~~~~~~~~~~~~~

Table title renders above the table. This confirms the CSS theme has been applied.

.. list-table:: Title
   :widths: 50 50
   :header-rows: 1

   * - Heading row 1, column 1
     - Heading row 1, column 2
   * - Row 1, column 1
     -
   * - Row 2, column 1
     - Row 2, column 2

Sidebar links
~~~~~~~~~~~~~

Sidebar links exist, and point to the ``beeware-theme`` repo. This confirms that the
sidebar content has been loaded, and the Github repo name has been set in the Sphinx
context.

Custom static content
~~~~~~~~~~~~~~~~~~~~~

The title of this section is rendered in dark red. This confirms that the docs project
can still provide static content.

Final Checks
~~~~~~~~~~~~

Navigate to BeeWare Theme Demo Section Two for the final checks.

.. toctree::
   :maxdepth: 2
   :hidden:

   section_two/index
   section_three/index