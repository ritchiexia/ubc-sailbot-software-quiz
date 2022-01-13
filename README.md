# Technical Quiz - UBC Sailbot Software

## Instructions

1. Clone this repository

2. Create a public repository

3. Change the "origin" remote to point to the public repository you created

4. Complete the Python functions in `standard_calc.py`

5. Write PyTest unit tests in `test_standard_calc.py`

6. Pushing your code will run a linter and your tests.
You can find the results in the Actions tab on GitHub.
    - To run these tests locally on your computer, execute the `flake8` and `pytest` commands in `.github/workflows/python-app.yml`:

        ```sh
        flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
        ```

        ```sh
        flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
        ```

        ```sh
        pytest
        ```

7. When you are done, send us your repository's link

## Resources

You may use any resources you find but must complete the quiz individually.
Here are some resources to get you started:

- [Python](https://www.python.org/about/gettingstarted/)
- [PyTest](https://docs.pytest.org/en/6.2.x/getting-started.html)
- [Flake8](https://flake8.pycqa.org/en/latest/)
- [GitHub Actions](https://docs.github.com/en/actions/quickstart#viewing-your-workflow-results)
