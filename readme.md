# QA Automation Project

This project demonstrates an automated testing framework built using Selenium and PyTest, following ISTQB standards. The goal is to automate the testing of key user flows, including login, search functionality, and checkout, while ensuring comprehensive test coverage.

## Project Overview

### This repository contains the code for end-to-end automated tests of a web application, focusing on:

- Functional testing
- Negative testing (invalid inputs, boundary cases)
- Regression testing
- Automated test reports with Allure

<hr>

## Test Plan

### 1. Test Objectives

- Ensure the correct functionality of login, product search, and checkout flows.
- Verify the application's behavior with both valid and invalid data inputs.
- Ensure error handling for empty or invalid form submissions is correct.

### 2. Scope of Testing

- **Included:**
  - Login functionality
  - Product search and filtering
  - Cart and checkout flow
  - Form validation and error handling
- **Excluded:**
  - Third-party payment gateways (for now)
  - Performance or load testing (future scope)

### 3. Test Levels

### The following levels of testing will be conducted:

- **Integration Testing:** Ensure interactions between login, search, and checkout components work as expected.
- **System Testing:** Validate that the entire user journey works correctly, from login to checkout.
- **Regression Testing:** Ensure that changes to the application do not break existing functionality.

### 4. Test Types

- **Functional Testing:** Verify that the core functionality (login, search, checkout) works correctly.
- **Negative Testing:** Test invalid inputs and ensure proper error handling.
- **Boundary Testing:** Use boundary value analysis to test input limits (e.g., field length limits).

### 5. Test Environment

### The automated tests will be run in the following environment:

- **Browser: Google Chrome**
- **Operating System: Ubuntu**
- **Test Data: Stored internally or via external files (CSV or JSON)**

### 6. Tools

- **Selenium WebDriver:** For browser automation
- **PyTest: For managing** and running test cases
- **Allure: For generating** detailed test reports

### Test Strategy

### 1. Test Approach

- **Automated End-to-End Testing:** We are automating key user flows such as login, product search, and checkout using Selenium and PyTest.
- **Negative Testing:** We are testing invalid inputs, such as incorrect usernames or empty fields, to ensure error handling works correctly.
- **Regression Testing:** When new features are added, we’ll rerun the tests to ensure that existing features still function as expected.

### 2. Entry and Exit Criteria

- **Entry Criteria:**
  - Application is deployed and stable.
  - All necessary test data is available.
- **Exit Criteria:**
  - All critical test cases have been executed.
  - No high-priority bugs remain open.
  - Detailed test reports have been generated and reviewed.

### 3. Risk Analysis

- **Potential Risks:**
  - Changes in the web application’s structure (DOM) could break automated tests.
  - Network or browser performance issues might affect test reliability.

### 4. Test Deliverables

- **Test Plan Document:** Outlining objectives, scope, risks, and strategy.
- **Test Scripts:** PyTest scripts to automate login, search, and checkout flows.
- **Test Reports:** Generated using Allure, containing pass/fail rates, test coverage, and identified bugs.

<hr>

## Test Design:

### 1. Equivalence Partitioning

**The following partitions will be tested for the login functionality:**

| **Username**    | **Password**   | **Expected Result**             |
| --------------- | -------------- | ------------------------------- |
| standard_user   | secret_sauce   | Successful login (dashboard)    |
| locked_out_user | secret_sauce   | Error message: Locked out       |
| invalid_user    | secret_sauce   | Error message: Invalid username |
| standard_user   | wrong_password | Error message: Invalid password |

### 2. Boundary Value Analysis

**For boundary testing, we are testing:**

- **Password length:** Test edge cases where the password length is just below and above the required limit (e.g., 7, 8, 9 characters).
- **Input length:** If a form field limits input to 50 characters, we test with 49, 50, and 51 characters.

### 3. Decision Table Testing

A decision table will be created to map input combinations and expected outcomes. This is applied to complex user interactions like login attempts.

<hr>

## How to Run the Tests

### 1. Install dependencies:

- Make sure you have Python installed.
- Install required libraries:

```
pip install -r requirements.txt
```

### 2. Run tests with PyTest:

```
pytest --alluredir=allure-results
```

### 3. View Allure Reports:

- To generate and view the Allure report:

```
allure serve allure-results
```

<hr>

## Contributing

- To contribute to this project, please submit a pull request with a detailed description of the changes.
- Ensure that all test cases pass before submitting your PR.
