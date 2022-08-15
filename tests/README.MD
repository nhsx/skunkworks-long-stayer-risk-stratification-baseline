# Integration tests

Once you have completed the [getting started](../README.md#getting-started) section of this project and activated your virtual environment, you can execute end-to-end integration test by running from the main project directory:

> Warning: the integration test may open a number of browser windows with plotly diagrams

```bash
cd tests
./integration_test.sh
```

This will perform the following actions:

1. Check for `../data` and `../models` directories
2. Generate fake data
3. Execute each notebook in turn
