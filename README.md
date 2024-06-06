# CS-1001-Testers

## Folder Structure

Each homework assignment has its own folder, named according to the assignment number (e.g., `hw1`, `hw2`, etc.). Inside each folder, you will find two files:

- `hw%_testers.py`: This file contains the test cases for the assignment.
- `skeleton_file.py`: This file is the skeleton code with placeholder functions that you need to implement.

The folder structure looks like this:

```
cs-1001-testers/
  ├── hw1/
  │   ├── hw1_testers.py
  │   └── skeleton_file.py
  ├── hw2/
  │   ├── hw2_testers.py
  │   └── skeleton_file.py
  └── hw3/
      ├── hw3_testers.py
      └── skeleton_file.py
  ...
```

## How to Clone the Repository

To get started, you need to clone this repository to your local machine. Open your terminal or command prompt and run the following command:

```bash
git clone https://github.com/yonatanmgr/cs-1001-testers.git
```

Navigate into the cloned directory:

```bash
cd cs-1001-testers
```

## How to Use

1. **Copy Your Implementations:**

   For each assignment, open the corresponding `skeleton_file.py` and paste your function implementations into this file. Each function initially contains a `pass` statement which you need to replace with your code.

   Example:
   ```python
   def example_function():
       # Replace 'pass' with your implementation
       pass
   ```

2. **Run the Testers:**

   After you have pasted your implementations, run the corresponding tester file to validate your solutions. 

   For example, if you are working on `hw1`, you would run: `python hw1/hw1_testers.py`

   This will execute the test cases and provide feedback on whether your functions are working correctly.

## Contribution

If you find any issues with the tester files or have suggestions for improvements, feel free to create an issue or submit a pull request.
