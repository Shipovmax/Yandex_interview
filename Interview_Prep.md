# Python Interview Preparation Guide

This guide covers common Python technical interview questions and detailed answers regarding language internals, concurrency, memory management, and best practices.

---

### Data Structures
*   **What is the difference between `list`, `tuple`, `set`, and `dict`?**
    *   **list:** Mutable ordered sequence. Allows duplicates. Access by index is O(1). Append is amortized O(1). Insert/delete in the middle is O(n).
    *   **tuple:** Immutable ordered sequence. Used for fixed collections of items. Can be used as `dict` keys if elements are hashable. Generally more memory-efficient than lists.
    *   **set:** Unordered collection of unique hashable elements. Fast membership testing, addition, and removal (~O(1)). Used for uniqueness and mathematical set operations (intersection, union).
    *   **dict:** Key-value mapping implemented as a hash table. In modern CPython (3.7+), it preserves insertion order. Key access is ~O(1).

*   **How do `@staticmethod`, `@classmethod`, and `@property` work?**
    *   **@staticmethod:** Defines a method that doesn't receive an implicit first argument (`self` or `cls`). It's just a function living in the class namespace.
    *   **@classmethod:** Defines a method that receives the class (`cls`) as the first argument. Useful for factory methods (alternative constructors).
    *   **@property:** Turns a method into a "getter" attribute. Can be combined with `.setter` and `.deleter` to encapsulate field access with attribute syntax.

*   **Difference between `is` and `==`?**
    *   `==` checks for **equality** (calls `__eq__`): do the objects have the same content?
    *   `is` checks for **identity**: do both variables point to the same object in memory (same `id()`)?

---

### Memory Management & Internals
*   **What is the GIL and why does it exist?**
    *   The **Global Interpreter Lock** (GIL) is a mutex in CPython that protects access to Python objects, preventing multiple native threads from executing Python bytecodes at once. It simplifies memory management (especially reference counting) and makes thread-safe operations on objects easier to implement.
    *   **Downside:** It prevents multi-core utilization for CPU-bound Python code.
    *   **Workarounds:** Use `multiprocessing`, C-extensions, or alternative implementations like PyPy (though it also has a GIL) or JPython.

*   **Threading vs. Multiprocessing?**
    *   **Threading:** Shared memory space, lightweight, low overhead. Best for I/O-bound tasks. Limited by GIL for CPU-bound tasks in CPython.
    *   **Multiprocessing:** Separate memory spaces (isolated), bypasses GIL by using separate interpreters per process. Best for CPU-bound tasks. Higher overhead for creation and Inter-Process Communication (IPC).

*   **How does the Garbage Collector (GC) work in Python?**
    *   CPython uses two main mechanisms:
        1.  **Reference Counting:** Objects are deallocated immediately when their reference count drops to zero.
        2.  **Generational GC:** Periodically detects and collects reference cycles (A points to B, B points to A) that reference counting can't handle. It uses three generations (0, 1, 2) to optimize performance by scanning newer objects more frequently.

*   **What are `__slots__`?**
    *   A declaration that tells Python not to use a dynamic `__dict__` for instances, but instead allocate a fixed amount of space for specific attributes. This saves significant memory for classes with many instances and can slightly improve attribute access speed.

---

### Concurrency
*   **What is `asyncio`, `await`, and the `event loop`?**
    *   **asyncio:** A library for writing concurrent code using the async/await syntax.
    *   **event loop:** The core of asyncio that manages and distributes the execution of different tasks. It registers, executes, and delays tasks based on events (like I/O readiness).
    *   **await:** Yields control back to the event loop, allowing other tasks to run while waiting for an operation (like a network request) to complete.

---

### Advanced Python Concepts
*   **Generators vs. Iterators?**
    *   **Iterator:** An object implementing `__iter__` and `__next__`.
    *   **Generator:** A special type of iterator created using a function with `yield` or a generator expression. They are "lazy" (compute values on the fly) and maintain their state between calls.

*   **What is MRO (Method Resolution Order)?**
    *   The order in which Python looks for a method in a class hierarchy. It uses the **C3 Linearization** algorithm to handle multiple inheritance consistently.

*   **What are Metaclasses?**
    *   A "class of a class" that defines how a class behaves. The default metaclass is `type`. You can create custom metaclasses to modify class creation (e.g., for validation or registration in frameworks).

*   **Decorators?**
    *   Functions that take another function and extend its behavior without explicitly modifying it. Syntax: `@decorator`. Essential to use `functools.wraps` to preserve the original function's metadata.

*   **`*args` vs. `**kwargs`?**
    *   `*args`: Collects extra positional arguments into a tuple.
    *   `**kwargs`: Collects extra keyword arguments into a dictionary.

---

### Best Practices & Optimization
*   **Type Annotations:** Metadata added to code (e.g., `x: int`) to help static analyzers (like mypy) and IDEs catch type-related bugs. They do not affect runtime performance.
*   **`"".join(list)` vs. `+` concatenation:** `join` is much faster (O(n)) because it calculates the total size once and performs a single allocation. Repeated `+` results in multiple allocations and copies (O(n²)).
*   **Profiling:** Use `cProfile` for function-level timing and `timeit` for micro-benchmarking small snippets. For memory, use `memory_profiler` or `tracemalloc`.

---

### Error Handling
*   **`try/except/finally/else`:**
    *   `try`: Code to monitor.
    *   `except`: Handles specific exceptions.
    *   `else`: Runs if no exception occurred.
    *   `finally`: Runs always (useful for cleanup).

*   **`raise` vs. `assert`:**
    *   `raise`: Explicitly triggers an exception in production logic.
    *   `assert`: Used for internal consistency checks during development; can be optimized away (removed) if Python is run with the `-O` flag.
