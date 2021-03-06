# hcdiagpy

This is meant as nothing more than a simple proof of concept for conversations.

## goal

The goal is to demonstrate something like a faster and more programmatic templating tool for hcdiag output.
This could be done in any language but I chose python for familiarity.
I feel like a better tool might be React or Svelte so that you could manipulate the DOM on-the-fly with text, formatting, etc directly in the browser.

## running

This is a python project built using poetry.
`poetry install` and the usual poetry workflow should work across all platforms.

The input is a Results.json from hcdiag.
The output is HTML in the build directory that sets up a basic page and then outputs the formatted Warning or Success message based on the Vault version being within minor - 2 of the current version (set in the code).

## examples

Screenshots are taken inside of Chrome's Print feature (which could also be used with something like Print to PDF)

![Passing page](screenshot_pass.png)

![Failing page](screenshot_fail.png)
