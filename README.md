# jotter
Note taking and syncing utility.

## Design

- `jotter init [REMOTE-URL]`
  - Create a jotter project (jotterproject.yml).
  - Git init.
  - If remote url is given then instead just git clone.
    - If clone didn't have jotterproject.yml then create one to 'adopt'.
- `jotter set-remote REMOTE-URL`
  - Set the git origin to the remote URL.
- `jotter note NOTE-PATH`
  - Create a note at the given path and open the configured editor.
  - If note already existed then open in edit mode.
  - Wait for close then git add and commit.
- `jotter sync`
  - Push/pull changes to/from remote.

- `jotterproject.yml`
  - `editor`: The command to run to open notes in an editor, i.e. `code` or `vim`.
  - `note_extension`: The extension to create notes with. Defaults to `.md`.