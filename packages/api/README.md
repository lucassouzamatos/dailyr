## Running
This will start and configure the database in the background and start the server listening in the terminal foreground, so you can see all incoming requests.

```bash
$ yarn dev
```

### Developer Troubleshooting
1. `ModuleNotFoundError` in your handler module:

R: Try renaming your module to something less usual. By now it is a bug inside serverless-offline plugin, in the way it handles calling the functions.

2. `Cannot do operations on a non-existent table`

R: This happens when the dynamodb plugin could not initialize the database correctly due to some error. Try first running `yarn db` which only starts the database, and the real problem should appear.
