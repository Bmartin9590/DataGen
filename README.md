# README for DataGen.py

## Overview

DataGen.py is a Python script designed to generate dummy data for a  hypothetical healthcare file uploading web application. The generated data is stored in a `.txt` file and includes fields necessary for compliance checking. This script is particularly useful for testing file parsing, validation, and compliance-checking functionalities in software systems. 

The script allows users to specify the number of records to generate and ensures that the data adheres to specific compliance rules. The generated file includes a header, data records, and a trailer, all formatted with pipe (`|`) delimiters. More compliance rules can be added or subtracted. Loops were used to help with specific compliance rules and can be edited/modified to fit different test cases. 

---

## Features
1. **Customizable Record Count**: Users can specify the number of records to generate.
    More can be added to be able to control certain specifications needed. 
2. **Unique Customer IDs**: Ensures all customer IDs are unique.
    Customer IDs are generated randomly. Logic can be added to ensure they never repeat if needed.
3. **Compliance Fields**: (to display examples of how to implement compliance specification or cater test cases.)
   - **Pregnant**: 
     - If `Sex` is `F`, the `pregnant` field is randomly assigned as `1=Yes` or `2=No`.
     - If `Sex` is `M`, the `pregnant` field is always `NULL`.
   - **In Care**:
     - Randomly assigned as `1=Yes`, `2=No`, or `3=Unknown`.
   - **Care Type**:
     - If `in_care` is `1`, the `care_type` field is randomly assigned as:
       - `A=cancer`, `B=heart`, `C=diabetes`, `D=mental health`, or `E=other`.
     - If `in_care` is `2` or `3`, the `care_type` field is set to `N/A`.
4. **File Structure**:
   - **Header**: Contains the project ID, record count, and the date the file was created.
   - **Data Records**: Includes fields such as project ID, customer ID, name, sex, birthday, address, compliance fields, etc.
   - **Trailer**: Contains the record count and the date the file was created.
5. **File Naming Convention**: The file is named as `<ProjectID>_<DateCreated>_<RecordCount>.txt` and saved in a 

testFiles

 folder.

---

## File Format
The generated `.txt` file is structured as follows:

### Header:
```
H|<ProjectID>|<RecordCount>|<DateCreated>
```

### Data Records:
```
<ProjectID>|<CustomerID>|<FirstName>|<LastName>|<Sex>|<Birthday>|<StreetAddress>|<City>|<State>|<Pregnant>|<InCare>|<CareType>
```

### Trailer:
```
T|<ProjectID>|<RecordCount>|<DateCreated>
```

---

## Compliance Checks
The script enforces the following compliance rules:
1. **Pregnant Field**:
   - If `Sex` is `F`, the `pregnant` field is randomly assigned as `1=Yes` or `2=No`.
   - If `Sex` is `M`, the `pregnant` field is always `NULL`.
2. **In Care and Care Type Fields**:
   - If `in_care` is `1`, the `care_type` field is randomly assigned as:
     - `A=cancer`, `B=heart`, `C=diabetes`, `D=mental health`, or `E=other`.
   - If `in_care` is `2` or `3`, the `care_type` field is set to `N/A`.

---

## How to Use
1. **Install Dependencies**:
   - Ensure Python is installed on your system.
   - Install the required libraries using:
     ```bash
     pip install faker
     ```

2. **Run the Script**:
   - Execute the script in your terminal:
     ```bash
     python3 dataGen.py
     ```
   - Enter the `Project ID` and the number of records to generate when prompted.

3. **Output**:
   - The generated file will be saved in the 

testFiles

 folder in the same directory as the script.

---

## Use Cases for Software Testing
1. **File Parsing**:
   - Test the ability of the application to parse and process files with structured data.
2. **Validation Testing**:
   - Verify that the application correctly enforces compliance rules (e.g., `pregnant` field logic, `care_type` logic).
3. **Stress Testing**:
   - Generate large datasets to test the application's performance and scalability.
4. **Error Handling**:
   - Use the generated data to test how the application handles invalid or edge-case data.
5. **Integration Testing**:
   - Simulate real-world scenarios by uploading the generated files to the application and verifying end-to-end functionality.

---

## Example Output
### Header:
```
H|AA5555|20|20250429
```

### Data Record:
```
AA5555|J21262|Jimmy|Hernandez|M|1971-01-10|8722 Richardson Fort|Joshuaside|Missouri|NULL|1|A
```

### Trailer:
```
T|20|20250429
```

---

## Notes
- The script ensures all customer IDs are unique.
- The 

testFiles

 folder is automatically created if it does not exist.
- The date format used is `YYYYMMDD` for consistency and sorting purposes.

---

## License
This script is open-source and can be freely used and modified for testing purposes.
