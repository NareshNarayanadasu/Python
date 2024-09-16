Here’s a detailed explanation of **positional arguments**, `*args`, `**kwargs`, and **mandatory arguments**, highlighting their differences:

### 1. **Positional Arguments:**
   - **Definition**: Arguments passed to a function in a defined order (position matters).
   - **Mandatory**: If a positional argument is defined in a function, it **must** be provided when calling the function.
   - **Example**:
     ```python
     def greet(name, message):
         print(f"Hello {name}, {message}")

     greet("Alice", "Good morning")  # Output: Hello Alice, Good morning
     ```
     Here, `name` and `message` are **positional arguments** and **mandatory**—they must be passed when the function is called.

### 2. **`*args` (Variable Positional Arguments)**:
   - **Definition**: Allows a function to accept any number of **positional** arguments. These arguments are collected into a tuple.
   - **Optional**: You don't have to pass any arguments if you don’t want to, but you can pass as many as needed.
   - **Example**:
     ```python
     def greet(*args):
         for arg in args:
             print(f"Hello {arg}")

     greet("Alice", "Bob", "Charlie")
     # Output:
     # Hello Alice
     # Hello Bob
     # Hello Charlie
     ```
     Here, `*args` allows passing a variable number of positional arguments.

### 3. **`**kwargs` (Variable Keyword Arguments)**:
   - **Definition**: Allows a function to accept any number of **keyword** arguments (name-value pairs). These arguments are collected into a dictionary.
   - **Optional**: You can pass as many keyword arguments as you want, or none at all.
   - **Example**:
     ```python
     def greet(**kwargs):
         for key, value in kwargs.items():
             print(f"{key}: {value}")

     greet(name="Alice", message="Good morning")
     # Output:
     # name: Alice
     # message: Good morning
     ```
     Here, `**kwargs` allows passing variable keyword arguments in the form of a dictionary.

### 4. **Mandatory Arguments**:
   - **Definition**: These arguments are explicitly required when calling a function, and must be provided.
   - **Example**:
     ```python
     def greet(name, age):
         print(f"Hello {name}, you are {age} years old.")

     greet("Alice", 25)  # Output: Hello Alice, you are 25 years old.
     ```
     In this case, both `name` and `age` are **mandatory arguments**.

### **Key Differences:**

| Concept           | Definition                                                                                        | Mandatory | Example                                                        |
|-------------------|---------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------------|
| **Positional**     | Arguments passed by their position in the function signature.                                      | Yes       | `greet("Alice", "Hello")`                                       |
| **`*args`**        | Collects **any number** of positional arguments into a tuple.                                      | No        | `greet("Alice", "Bob", "Charlie")`                              |
| **`**kwargs`**     | Collects **any number** of keyword arguments into a dictionary.                                    | No        | `greet(name="Alice", message="Good morning")`                   |
| **Mandatory**      | These are arguments that must be provided in the function call for it to work.                     | Yes       | `greet("Alice", 25)`                                            |

### Combined Example:
You can combine all types of arguments in one function.

```python
def example_func(positional_arg, *args, mandatory_arg, **kwargs):
    print(f"Positional Arg: {positional_arg}")
    print(f"Args: {args}")
    print(f"Mandatory Arg: {mandatory_arg}")
    print(f"Kwargs: {kwargs}")

example_func("pos1", "arg1", "arg2", mandatory_arg="must_be_provided", kwarg1="val1", kwarg2="val2")
```

### Output:
```
Positional Arg: pos1
Args: ('arg1', 'arg2')
Mandatory Arg: must_be_provided
Kwargs: {'kwarg1': 'val1', 'kwarg2': 'val2'}
```

- The first argument is a **positional argument**.
- `"arg1"` and `"arg2"` go into `*args`.
- `mandatory_arg` must be provided.
- Any remaining keyword arguments go into `**kwargs`.
