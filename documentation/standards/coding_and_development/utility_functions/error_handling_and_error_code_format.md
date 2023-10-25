# Error Handling and Error Code Format Guidelines

## Introduction
Error handling is a vital aspect of robust software, especially in complex systems like Project Kami. This document outlines the standardized approach to error handling and error code formatting, incorporating the new error code strategy.

## Error Handling
- Incorporate try-except blocks in methods that might raise exceptions.
- In the exception block, call `print_tracer` with the "Error" event.
- Handle the error using the standardized `handle_error` function. Ensure this method is part of the utilities and imported wherever needed.

## Error Code Format
- Each error should have a unique code, following the newly proposed format. The base error code is set at the class level, and unique numbers are appended for each method within the class.
- Update the central `ERROR_CODES` dictionary (located in `constants/error_codes.py`) whenever a new error is defined.


## Example Python Implementation
```python
class ExampleClass:
    BASE_ERROR_CODE = "EXM"

    def risky_method(self):
        METHOD_ERROR_NUM = "001"
        try:
            # some risky operation
        except Exception as e:
            complete_error_code = self.BASE_ERROR_CODE + METHOD_ERROR_NUM
            handle_error(complete_error_code)
            # Update 'constants/error_codes' dictionary


## Future Tasks
- [ ] Extend error handling to other programming languages.
- [ ] Develop a mechanism for dynamic addition of third-party error codes.
- [ ] Create a centralized ERROR_CODES dictionary.
