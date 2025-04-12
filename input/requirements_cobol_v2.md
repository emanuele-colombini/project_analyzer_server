# Insurance Policy Processing System Technical Documentation

**Table of Contents**

1.  Executive Summary
2.  System Overview
3.  System Architecture

    * 3.1 Architecture Overview
    * 3.2 Main Components
    * 3.3 Database Integration
    * 3.4 Architecture Diagram
4.  Processing Flows

    * 4.1 Policy Processing
    * 4.2 Premium and Coverage Calculation
    * 4.3 Geographic Data Management
    * 4.4 Agency Management
    * 4.5 Catastrophe Modeling Records
    * 4.6 Currency Conversion
5.  Data Model

    * 5.1 Main Table Structure
    * 5.2 Entity Relationships
    * 5.3 Data Dictionary
6.  Technical Components

    * 6.1 Data Access Modules
    * 6.2 Date and Time Utilities
    * 6.3 Calculation Functions
    * 6.4 Error Management
7.  Integrations

    * 7.1 External Systems
    * 7.2 Data Interfaces
8.  Glossary

## 1. Executive Summary

This document provides a detailed technical description of an insurance policy processing system implemented in a COBOL mainframe environment. [cite: 1, 2, 3] The system handles various aspects of the policy lifecycle, including creation, modification, retrieval, and calculation of premiums and coverages. [cite: 1, 2, 3] The system interacts with multiple databases, including DB2 and IMS, and utilizes various COBOL programs and subroutines to implement business logic. [cite: 3]

The system is designed to handle a variety of policy types and coverage scenarios, including coinsurance, direct and indirect damages, and different risk classes. [cite: 4, 5] It incorporates complex calculations to determine premiums, deductibles, and maximum coverage limits based on factors such as location, property type, and sum insured. [cite: 4, 5] The system also handles currency conversion and generates records for catastrophe modeling. [cite: 6]

This document describes the system architecture, processing flows, data model, technical components, integrations, and a glossary of terms. [cite: 7, 8] It provides a comprehensive understanding of the system and its capabilities, serving as a valuable resource for developers, business analysts, and other stakeholders involved in maintaining and enhancing the system. [cite: 7, 8]

## 2. System Overview

The policy processing system is a central component of an insurance company's IT infrastructure. [cite: 9, 10] Its primary purpose is to automate and manage the lifecycle of insurance policies, from creation to termination. [cite: 9, 10] The system encompasses the following key aspects:

* Policy Creation: Captures and validates policy data, including insured details, coverage, sum insured, and policy parameters. [cite: 11]
* Policy Modification: Allows modifications to existing policies, such as changes to coverage, sum insured, or insured details. [cite: 12, 13]
* Policy Retrieval: Provides access to policy data for inquiry, reporting, and claims processing. [cite: 12, 13, 14]
* Premium Calculation: Calculates premiums based on various factors, including policy type, coverage, sum insured, location, and risk class. [cite: 14]
* Coinsurance Management: Handles coinsurance scenarios, calculating each coinsurer's premium share and liability. [cite: 15, 16, 17, 18, 19, 20, 21]
* Damage Management: Processes direct and indirect damages, determining coverage and calculating payments. [cite: 15, 16, 17, 18, 19, 20, 21]
* Agency Management: Handles primary and subsidiary agencies, including their codes and types. [cite: 15, 16, 17, 18, 19, 20, 21]
* Catastrophe Modeling: Generates records for catastrophe modeling, providing data for risk assessment and disaster management planning. [cite: 15, 16, 17, 18, 19, 20, 21]
* Currency Conversion: Handles currency conversion for policies in different currencies. [cite: 15, 16, 17, 18, 19, 20, 21]

The system is designed to be robust, accurate, and efficient, ensuring timely and precise processing of insurance policies. [cite: 20, 21, 22] It supports a variety of policy types and coverage scenarios, meeting the diverse needs of the insurance company and its clients. [cite: 20, 21, 22]

## 3. System Architecture

### 3.1 Architecture Overview

The policy processing system is built upon a COBOL mainframe architecture, leveraging the transaction processing capabilities and reliability of mainframe systems. [cite: 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33] The system architecture can be characterized as a multi-tiered architecture, with the following key components:

* Presentation Layer: There is no dedicated presentation layer in this system, as it is primarily a batch processing system. [cite: 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33] Interaction with the system is through batch jobs and input files. [cite: 24, 25, 26, 27, 28, 29, 30, 31, 32, 33]
* Business Logic Layer: This layer is implemented using COBOL programs and subroutines. [cite: 24, 25, 26, 27, 28, 29, 30, 31, 32, 33] It handles the core business logic of the system, including policy processing, premium calculations, coinsurance management, and report generation. [cite: 26, 27, 28, 29, 30, 31, 32, 33]
* Data Access Layer: This layer provides access to the system's databases, including DB2 and IMS. [cite: 28, 29, 30, 31, 32, 33] It uses COBOL data access modules and DL/I calls to interact with the databases. [cite: 28, 29, 30, 31, 32, 33]
* Database Layer: This layer consists of the system's databases, which store policy data, customer data, agency data, and other related data. [cite: 30, 31, 32, 33] The databases are managed using DB2 and IMS. [cite: 30, 31, 32, 33]

The system architecture is designed to be modular and flexible, allowing for the addition of new components and functionality over time. [cite: 31, 32, 33] The layered architecture promotes separation of concerns, making the system easier to maintain and enhance. [cite: 31, 32, 33]

### 3.2 Main Components

The policy processing system comprises various COBOL modules and components that work together to implement the system's functionality. [cite: 33, 34, 35, 36, 37, 38, 39, 40, 41] The main components include:

* Policy Processing Modules: These modules handle the core business logic related to policy processing, including creation, modification, retrieval, and calculations. [cite: 33, 34, 35, 36, 37, 38, 39, 40, 41]
    * EDARAP01: Generalized BATCH routine for GNP and GHNP. [cite: 35, 36, 37, 38, 39, 40, 41] Handles database operations on various tables related to insurance policies. [cite: 35, 36, 37, 38, 39, 40, 41]
    * EDARAPO2: Generalized BATCH routine for GNP and GHNP. [cite: 35, 36, 37, 38, 39, 40, 41] Retrieves and manipulates insurance policy data. [cite: 35, 36, 37, 38, 39, 40, 41]
    * EDARAP03: Generalized BATCH routine for GNP and GHNP. [cite: 35, 36, 37, 38, 39, 40, 41] Performs database operations related to insurance policies, including managing parent-child relationships. [cite: 35, 36, 37, 38, 39, 40, 41]
    * EDARAG01: Generalized BATCH routine for GU and GHU. [cite: 35, 36, 37, 38, 39, 40, 41] Retrieves data from RDBMS tables based on keys and maps them to IMS/DB segments. [cite: 38, 39, 40, 41]
    * EDARTG01: Generalized BATCH routine for GU and GHU. [cite: 38, 39, 40, 41] Retrieves data from various tables based on provided keys and conditions. [cite: 38, 39, 40, 41]
    * EDARAF01: Generalized BATCH routine for GN and GHN. [cite: 38, 39, 40, 41] Performs database operations on various tables related to insurance policies, including managing cursors and key areas. [cite: 38, 39, 40, 41]
* Data Access Modules: These modules provide access to the system's databases, encapsulating the database interaction logic. [cite: 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]
    * ELSRQ014: Retrieves data from the root segment of a technical database based on input criteria. [cite: 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]
    * EDLRFU3A: Retrieves data from the TPT\_SOMMA\_FATTORE table based on different access methods. [cite: 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]
    * EDLR1F05: Accesses an administrative database to retrieve policy information, specifically the policy's company code. [cite: 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]
    * EDLRWF79: Retrieves a geolocation record from the TUT\_GEOLOCALIZZAZIONE table based on provided contract code, component code, and insertion timestamp. [cite: 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53]
    * EDLRUF44: Retrieves data from the OSP.TLT\_GPERS\_CAT\_TRAS\_RT\_OC table based on various input criteria. [cite: 46, 47, 48, 49, 50, 51, 52, 53]
    * EDLRTF52: Reads data from a table named TPT\_SOMMA in a DB2 database. [cite: 46, 47, 48, 49, 50, 51, 52, 53] Supports random access based on a key and sequential access using a cursor. [cite: 47, 48, 49, 50, 51, 52, 53]
* Date and Time Utilities: These modules provide functions for manipulating dates and timestamps, including date validation, date difference calculation, and timestamp generation. [cite: 49, 50, 51, 52, 53]
    * IYYCRDA8: Validates a date in 'YYMMDD' format. [cite: 49, 50, 51, 52, 53]
    * PLSYUT35: Generates a timestamp by combining the current date and time. [cite: 50, 51, 52, 53]
    * PLSYUT36: Decodes a timestamp into its component parts: year, month, day, hour, minute, second, and hundredth of a second. [cite: 50, 51, 52, 53]
    * PLSYUT68: Decodes an 8-byte internal timestamp to a 26-byte external timestamp for DB2. [cite: 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
    * PLSYUT74: Determines whether a year is a leap year. [cite: 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
* Calculation Functions: These modules perform mathematical and financial calculations, including premium calculations, deductibles, and currency conversions. [cite: 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
    * EGERVL01: Determines exchange rates between the Italian lira and other currencies. [cite: 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
    * EGERVL03: Handles currency conversions and calculations. [cite: 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
    * KRPD0077: Calculates the risk class of the main risk of an insurance policy. [cite: 54, 55, 56, 57, 58, 59, 60, 61, 62, 63]
    * KRPD0339: Calculates the company code and centralized code based on an environment flag. [cite: 56, 57, 58, 59, 60, 61, 62, 63]
    * KRPD0418: Retrieves rates, deductibles, limits, and territorial classes based on location and insurance policy details. [cite: 56, 57, 58, 59, 60, 61, 62, 63]
    * KRPM1112: Retrieves information about a location (comune) from the TUT\_TERRITORIO table based on provided location name, postal code, and province. [cite: 58, 59, 60, 61, 62, 63]
    * PLSYUTG0: Rounds a number to a specific number of decimals based on the currency code. [cite: 59, 60, 61, 62, 63]
    * PLSYUTG2: Rounds a number to a specific number of decimals (o to 3). [cite: 60, 61, 62, 63]
* Error Handling Modules: These modules handle errors and exceptions, including error logging, abnormal termination handling, and error message display. [cite: 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
    * ADRABND: Displays an error message and terminates the program abnormally (ABEND). [cite: 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
* Other Modules: The system also utilizes various other modules for tasks such as parsing JCL parameters, managing inter-program communication, and interacting with external systems. [cite: 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71]
    * ELSBPLG1: Processes transactions from a database, likely for report generation.
    * ELSBPLG4: Processes transactions from a database, likely for report generation.
    * ESTPC117: Processes insurance policy data to calculate premiums, deductibles, and maximum coverage amounts for various perils.
    * ESTPC142: Processes insurance policy data to generate output records for catastrophe modeling.
    * ESTPCATM: Processes insurance policy data to calculate premiums, deductibles, and maximum coverage amounts for different perils, handling currency conversions and generating output records.
    * ESTPCATC: Extracts insurance policy data from multiple databases, applies business rules to calculate policy parameters, and generates output records for further processing.

These components work together to provide a comprehensive solution for insurance policy processing. The system's modular architecture allows for code reuse and facilitates maintenance and enhancements.

### 3.3 Database Integration

The policy processing system interacts with multiple databases to retrieve and store data. The main databases used are:

* DB2: A relational database used to store policy data, customer data, agency data, and other related data. The system uses embedded SQL statements to interact with DB2.
* IMS: A hierarchical database used to store technical data and other policy-related data. The system uses <span class="math-inline">DL/I</span> calls to interact with IMS.

In addition to DB2 and IMS, the system may also interact with other databases and files using various data access methods. The COBOL data access modules encapsulate the database interaction logic, providing a consistent interface for accessing data from different sources. The integration with multiple databases allows the system to access and process data from various systems, providing a comprehensive view of policy data. However, it also introduces complexity and dependencies into the system architecture.

### 3.4 Architecture Diagram

**Components and Relations:**

* **Policy Processing (COBOL):** This is the core of the system. It is responsible for creating, modifying, retrieving, and calculating policy data. [cite: 34] It orchestrates the overall policy processing workflow by calling upon other specialized COBOL components to handle specific tasks. [cite: 34]
* **Online Processing (COBOL):** This component handles real-time policy-related requests. [cite: 34] When a user or another system needs immediate access to policy information or needs to initiate a real-time policy transaction, "Online Processing" receives and processes that request. [cite: 34] It then sends specific policy processing requests to the "Policy Processing" component to execute the necessary actions. [cite: 34]
* **Batch Processing (COBOL):** This component is designed to process policy transactions in batches. [cite: 34] For example, end-of-day processing, periodic updates, or large data updates are handled by "Batch Processing." [cite: 34] Similar to "Online Processing," it sends policy processing requests to the "Policy Processing" component, but for batch-oriented tasks. [cite: 34]
* **Calculations (COBOL):** This component provides calculation functionalities to the system. [cite: 34] "Policy Processing" uses "Calculations" to perform complex calculations such as premium calculations, deductible calculations, and currency conversions. [cite: 34, 54, 55, 56, 57, 58, 59, 60]
* **Geographic Data Management (COBOL):** This component is responsible for processing territorial and geolocation information. [cite: 34] "Policy Processing" utilizes "Geographic Data Management" to manage location-based data, which is crucial for risk assessment and premium calculation. [cite: 104, 105, 106, 107, 108, 109, 110, 111]
* **Data Access (COBOL):** This component acts as an abstraction layer for database interactions. [cite: 34] "Policy Processing" relies on "Data Access" to retrieve and store data in both the "IMS" and "DB2" databases. [cite: 28, 29, 30, 31] This component hides the complexities of database access from "Policy Processing." [cite: 41, 42, 43, 44, 45, 46, 47, 48, 49]
* **Agency Management (COBOL):** This component handles information related to the insurance company's agencies (main and subsidiary). [cite: 34] "Policy Processing" uses "Agency Management" to manage data about agencies, such as their codes, locations, and relationships. [cite: 112, 113, 114, 115, 116, 117, 118, 119]
* **Catastrophe Modeling (COBOL):** This component generates records that are used for catastrophe modeling. [cite: 34] "Policy Processing" uses "Catastrophe Modeling" to create the necessary data for risk assessment and disaster recovery planning. [cite: 120, 121, 122, 123, 124, 125, 126, 127, 128, 129]
* **Currency Conversion (COBOL):** This component handles the exchange rates and currency conversions. [cite: 34] When dealing with policies in different currencies, "Policy Processing" uses "Currency Conversion" to perform the necessary conversions. [cite: 130, 131, 132, 133, 134, 135, 136, 137]
* **Error Management (COBOL):** This component is responsible for handling errors and exceptions that occur during policy processing. [cite: 34, 61, 62, 63] "Policy Processing" uses "Error Management" to ensure that errors are properly logged, handled, and reported. [cite: 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216]
* **Date and Time Utilities (COBOL):** This component provides utility functions for working with dates and times. [cite: 34] "Policy Processing" uses "Date and Time Utilities" to validate dates, calculate date differences, and perform other date/time-related operations. [cite: 49, 50, 51, 52, 53, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193]
* **IMS:** This is a hierarchical database that stores evidence policy data. [cite: 74, 75] "Data Access" is the component that interacts with "IMS" to retrieve and store this specific type of policy information. [cite: 28, 29, 30, 31]
* **DB2:** This is a relational database that stores a broader range of data, including policy data, customer information, agency details, and reference tables. [cite: 72, 73] "Data Access" also interacts with "DB2" to manage this data. [cite: 28, 29, 30, 31]

**Data Flow:**

The data flow within the system is as follows:

1.  **Requests to Policy Processing:** "Online Processing" and "Batch Processing" initiate policy processing by sending requests to the central "Policy Processing" component. [cite: 24, 25, 80, 81, 82, 83, 84]
2.  **Orchestration by Policy Processing:** "Policy Processing" receives these requests and determines the necessary steps to fulfill them. [cite: 34] It then calls upon the appropriate specialized COBOL components to perform those steps. [cite: 34]
3.  **Component Interactions:**
    * "Policy Processing" uses "Calculations" to perform any required mathematical or financial calculations. [cite: 34, 54, 55, 56, 57, 58, 59, 60, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103]
    * "Policy Processing" uses "Geographic Data Management" to handle any processing related to location-based information. [cite: 34, 104, 105, 106, 107, 108, 109, 110, 111]
    * "Policy Processing" uses "Data Access" to retrieve or store data in the "IMS" or "DB2" databases. [cite: 34, 71, 72, 73, 74, 75]
    * "Policy Processing" uses "Agency Management" to manage any data related to agencies. [cite: 34, 112, 113, 114, 115, 116, 117, 118, 119]
    * "Policy Processing" uses "Catastrophe Modeling" to generate data for risk assessment. [cite: 34, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129]
    * "Policy Processing" uses "Currency Conversion" to handle any currency-related operations. [cite: 34, 130, 131, 132, 133, 134, 135, 136, 137]
    * "Policy Processing" uses "Error Management" to handle any errors that occur during processing. [cite: 34, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216]
    * "Policy Processing" uses "Date and Time Utilities" to perform any date or time-related tasks. [cite: 34, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193]
4.  **Database Interaction:** The "Data Access" component is the sole interface between the COBOL programs and the databases. [cite: 34, 76, 77, 78] It retrieves data from "IMS" and "DB2" and sends data to be stored in these databases. [cite: 34, 28, 29, 30, 31]
5.  **External System Interaction:** "Online Processing" and "Batch Processing" may also read data from and write data to external systems, although the specifics of these interactions are not detailed in this diagram.

Dependencies:

## 4. Processing Flows

### 4.1 Policy Processing

The workflow for processing insurance policies involves the following steps:

1.  Policy Data Reception: The system receives policy data from various channels, including online applications, agent systems, and batch jobs.
2.  Data Validation: The policy data is validated to ensure accuracy and integrity. This includes checking for required fields, data formats, and business rules.
3.  Policy Record Creation: Once the data is validated, policy records are created in the system's databases. This includes creating records in DB2 for the main policy data and in IMS for the technical data.
4.  Premium Calculation: Premiums are calculated based on the policy parameters, coverage, sum insured, location, and risk class. The system uses various calculation modules to perform these calculations.
5.  Coinsurance Management: If the policy involves coinsurance, the system calculates each coinsurer's premium share and liability.
6.  Document Generation: The system generates various policy-related documents, including policies, endorsements, and insurance certificates.
7.  Policy Record Updates: Policy records are updated to reflect changes to the policy, such as endorsements, renewals, or cancellations.
8.  Claims Processing: When a claim is filed, the system retrieves the policy data and uses it to assess coverage and process the claim.

The policy processing workflow is designed to be efficient and accurate, ensuring timely and correct processing of insurance policies.

### 4.2 Premium and Coverage Calculation

Premium and coverage calculation is a crucial aspect of the policy processing system. The system uses complex business logic to determine premiums, deductibles, and maximum coverage limits based on various factors. These factors include:

* Policy Type: Different policy types have different premium structures and calculation rules.
* Coverage: The specific coverage included in the policy affects the premium. For example, a policy with flood damage coverage will have a higher premium than a policy without it.
* Sum Insured: The sum insured is the maximum amount the insurer will pay in case of loss. A higher sum insured leads to a higher premium.
* Location: The location of the insured property affects the premium. For example, a property located in a flood-prone area will have a higher premium than a property located in a low-risk area.
* Risk Class: The risk class is assigned to the policy based on the insured's risk profile. Higher-risk insureds pay higher premiums.

The system uses a combination of lookup tables, formulas, and business rules to calculate premiums and coverages. The calculation modules retrieve the necessary data from the databases and perform the required calculations. The business logic is designed to be accurate and consistent with the insurance company's underwriting practices.

### 4.3 Geographic Data Management

The policy processing system incorporates geographic data management to determine territorial classes, rates, and coverages based on the location of the insured property. The system uses the following geographic data:

* Postal Codes: Postal codes are used to identify specific geographic areas.
* Provinces: Provinces are broader administrative divisions than postal codes.
* Cresta Zones: Cresta zones are geographic regions classified based on their risk of natural catastrophes, such as floods and earthquakes.

The system retrieves the geographic data from the databases and uses it to determine the territorial class of the location. The territorial class is then used to look up the appropriate rates and coverages for the policy. The system may also use geographic data to validate the property's location and ensure it is within the insurer's coverage area.

Geographic data management allows the system to calculate accurate premiums and coverages based on the location of the insured property. It also helps the insurer assess and manage its risk exposure in different geographic regions.

### 4.4 Agency Management

The policy processing system manages the primary and subsidiary agencies that sell insurance policies on behalf of the insurer. The system stores information about each agency, including:

* Agency Code: A unique identifier for the agency.
* Agency Name: The name of the agency.
* Agency Type: Whether the agency is a main branch or a subsidiary.
* Agency Location: The address and contact details of the agency.

The system uses the agency data for various purposes, including:

* Policy Assignment: Policies are assigned to the agency that sold them.
* Commission Calculation: Commissions are calculated based on the agency's sales.
* Report Generation: Reports are generated to track agency performance.

The system allows the insurer to manage its relationships with agencies and track their sales and performance. It also provides data for commission calculation and report generation.

### 4.5 Catastrophe Modeling Records

The policy processing system generates records for catastrophe modeling, providing data for risk assessment and disaster management planning. The records contain information about the policies, the insured properties, and the potential perils. The perils covered include:

* Flood: The system calculates flood risk exposure based on the property's location and the policy characteristics.
* Earthquake: The system calculates earthquake risk exposure based on the property's location and the policy characteristics.
* Wind: The system calculates wind risk exposure based on the property's location and the policy characteristics.
* Hail: The system calculates hail risk exposure based on the property's location and the policy characteristics.
* Other Perils: The system may also generate records for other perils, such as fire, theft, and liability.

The records are generated in a specific format that can be used by catastrophe models to estimate potential losses from various catastrophic events. These models help the insurer assess its risk exposure, price policies appropriately, and develop risk management strategies.

Catastrophe modeling record generation is an essential component of the policy processing system, allowing the insurer to proactively manage its risk exposure and ensure its financial sustainability.

### 4.6 Currency Conversion

The policy processing system handles currency conversion for policies issued in different currencies. The system uses the following components for currency conversion:

* Exchange Rate Table: The system maintains an exchange rate table that stores the current exchange rates for different currency pairs.
* Currency Conversion Modules: The system uses currency conversion modules to convert amounts from one currency to another. These modules retrieve the exchange rates from the exchange rate table and perform the necessary calculations.

When processing a policy in a foreign currency, the system converts the relevant amounts, such as the premium, sum insured, and deductibles, to the insurer's base currency. This ensures that all calculations and financial reporting are done in a single currency.

The currency conversion system is designed to be accurate and reliable, ensuring that currency conversions are performed using the most up-to-date exchange rates. This is essential for maintaining the accuracy of the insurer's financial records.

## 5. Data Model

### 5.1 Main Table Structure

The policy processing system uses several database tables to store policy data and related information. The key tables include:

* TPA\_RADICE: This table stores the basic policy information, including the policy number, policy version, confidentiality level, origin, and timestamps.
* TPA\_RATA: This table stores information about policy installments, including the policy number, revision key, competence start date, competence end date, timestamps, and status.
* TPT\_SOMMA\_FATTORE: This table stores information about policy sum factors, including the policy number, component code, insertion timestamp, revision key, sub-revision key, factor ID, format code, factor description, policy band partition, factor value, factor category, and factor value description.
* TPT\_SOMMA: This table stores information about policy sums, including the policy number, component code, insertion timestamp, revision key, sub-revision key, sum code, program code, territorial extension, sum insured, count code, count amount, count coefficient, deductible amount, uncovered percentage, minimum uncovered, maximum uncovered, main risk, risk category, rate code, rate percentage, unit premium, annual taxable premium amount, accounting class, deductible days, net rate percentage, premium rate type, variable premium amount, policy band partition, user who inserted the record, and sum expiry date.
* TUT\_GEOLOCALIZZAZIONE: This table stores geolocation information, including the contract code, component code, insertion timestamp, and other location-related details.
* OSP.TLT\_GPERS\_CAT\_TRAS\_RT\_OC: This table stores information about risk types, occupation codes, and other policy-related data.
* TLT\_ITBTABEL: This table stores various reference data, including information about currencies, exchange rates, and other system parameters.

These tables are interrelated through foreign keys, creating a relational data model that supports the system's functionality. The data model is designed to be efficient and scalable, allowing the system to handle large volumes of policy data.

### 5.2 Entity Relationships

* **TPA\_RADICE:** This table appears to be the root or main policy table.
    * `NUM_POLIZZA`: VARCHAR (Policy Number - likely the primary key)
    * `VERSIONE_POLIZZA`: VARCHAR (Policy Version)
    * `LIVELLO_CONFID`: VARCHAR (Confidentiality Level)
    * `PROVENIENZA_8100`: VARCHAR (Origin - possibly related to the system or source)
    * `TMS_APPEND_TECN`: TIMESTAMP (Technical Append Timestamp)
    * `PRIMO_APPEND_TECN`: TIMESTAMP (First Technical Append Timestamp)
    * `NUM_APPEND_REGOL`: INT (Regulatory Append Number)
    * `TMS_AGGIORN`: TIMESTAMP (Update Timestamp)
    * `UTENTE_AGG`: VARCHAR (User who updated)
    * `TMS_ULT_PROG_SAG`: TIMESTAMP (Last SAG Program Timestamp)
    * `UTENTE_FASCIA_POL`: VARCHAR (Policy Band User)
    * `TMS_INIZIO_VALIDITA`: TIMESTAMP (Start Validity Timestamp)
    * `TMS_ANNULLAZIONE`: TIMESTAMP (Cancellation Timestamp)
    * **Relationships:**
        * Has a relationship (indicated by a connecting line) with `TPA_RATA`.
        * Has a relationship (indicated by a connecting line) with `TPT_SOMMA`.
        * Has a relationship (indicated by a connecting line) with `OSP.TLT_GPERS_CAT_TRAS_RT_OC` (though the specifics of the relationship aren't detailed in terms of foreign keys in this view).

* **TPA\_RATA:** This table likely stores installment information for policies.
    * `NUM_POLIZZA`: INT (Policy Number - likely a foreign key referencing `TPA_RADICE`)
    * `REVKEY`: INT (Revision Key - possibly part of the primary key or used for tracking changes)
    * `DATA_INIZ_COMPET`: DATE (Competence Start Date)
    * `DATA_FINE_COMPET`: DATE (Competence End Date)
    * `TMS_INIZIO_VALIDITA`: TIMESTAMP (Start Validity Timestamp)
    * `TMS_FINE_VALIDITA`: TIMESTAMP (End Validity Timestamp)
    * `STATO`: VARCHAR (Status)
    * **Relationships:**
        * Has a relationship (indicated by a connecting line) with `TPA_RADICE`, likely a one-to-many relationship where one policy (`TPA_RADICE`) can have multiple installments (`TPA_RATA`).

* **TPT\_SOMMA\_FATTORE:** This table likely stores factors that contribute to the policy sum or premium calculation.
    * `NUM_POLIZZA`: INT (Policy Number - likely a foreign key referencing `TPA_RADICE`)
    * `COD_COMPON`: INT (Component Code - identifies a specific part of the policy)
    * `TMS_INSERIMENTO`: TIMESTAMP (Insertion Timestamp - likely part of the primary key or used for tracking)
    * `REVKEY`: INT (Revision Key - likely part of the primary key or used for tracking)
    * `REVKEY_SUB`: INT (Sub-Revision Key - likely part of the primary key or used for tracking)
    * `ID_FATTORE`: INT (Factor ID)
    * `COD_FORMATO`: VARCHAR (Format Code)
    * `DESCR_FATTORE`: VARCHAR (Factor Description)
    * `VALORE_FATTORE`: VARCHAR (Factor Value)
    * `CATEGORIA_FATTORE`: VARCHAR (Factor Category)
    * `DESCR_VAL_FATTORE`: VARCHAR (Factor Value Description)
    * **Relationships:**
        * Has a relationship (indicated by a connecting line) with `TPT_SOMMA`, likely a one-to-many relationship where one policy sum (`TPT_SOMMA`) can have multiple factors (`TPT_SOMMA_FATTORE`).

* **TPT\_SOMMA:** This table likely stores information about policy sums insured, premiums, and related details.
    * `NUM_POLIZZA`: INT (Policy Number - likely a foreign key referencing `TPA_RADICE`)
    * `COD_COMPON`: INT (Component Code)
    * `TMS_INSERIMENTO`: TIMESTAMP (Insertion Timestamp - likely part of the primary key or used for tracking)
    * `REVKEY`: INT (Revision Key - likely part of the primary key or used for tracking)
    * `REVKEY_SUB`: INT (Sub-Revision Key - likely part of the primary key or used for tracking)
    * `COD_SOMMA`: VARCHAR (Sum Code)
    * `ESTENSIONE_TERRIT`: VARCHAR (Territorial Extension)
    * `SOMMA_ASSICURATA`: DECIMAL (Sum Insured)
    * `COD_CONTEGGIO`: VARCHAR (Count Code)
    * `IMPORTO_CONTEGGIO`: DECIMAL (Count Amount)
    * `COEFF_CONTEGGIO`: DECIMAL (Count Coefficient)
    * `IMPORTO_FRANCHIGIA`: DECIMAL (Deductible Amount)
    * `SCOPERTO_MINIMO`: DECIMAL (Minimum Uncovered Amount)
    * `SCOPERTO_MASSIMO`: DECIMAL (Maximum Uncovered Amount)
    * `PERC_SCOPERTO`: DECIMAL (Uncovered Percentage)
    * `PRINCIPALE_RISCHIO`: VARCHAR (Main Risk)
    * `CATEG_RISCHIO`: VARCHAR (Risk Category)
    * `COD_TARIFFA`: VARCHAR (Rate Code)
    * `PERC_TASSO`: DECIMAL (Rate Percentage)
    * `PREMIO_UNITARIO`: DECIMAL (Unit Premium)
    * `PREMIO_IMP_ANNUO`: DECIMAL (Annual Taxable Premium Amount)
    * `CLASSE_CONTAB`: VARCHAR (Accounting Class)
    * `GIORNI_FRANCHIGIA`: INT (Deductible Days)
    * `TASSO_NETTO`: DECIMAL (Net Rate Percentage)
    * `TIPO_TASSO_PREMIO`: VARCHAR (Premium Rate Type)
    * `IMPORTO_PREMIO_VAR`: DECIMAL (Variable Premium Amount)
    * `PARTIZ_FASCIA_POL`: VARCHAR (Policy Band Partition)
    * `UTENTE_INSERIMENTO`: VARCHAR (User who inserted)
    * `DATA_SCAD_SOMMA`: DATE (Sum Expiry Date)
    * `FLAG_RINNOVABILITA`: VARCHAR (Renewability Flag)
    * **Relationships:**
        * Has a relationship (indicated by a connecting line) with `TPA_RADICE`, likely a one-to-many relationship where one policy (`TPA_RADICE`) can have multiple sums (`TPT_SOMMA`).
        * Has a relationship (indicated by a connecting line) with `TPT_SOMMA_FATTORE`, likely a one-to-many relationship where one policy sum (`TPT_SOMMA`) can have multiple factors (`TPT_SOMMA_FATTORE`).
        * Has a relationship (indicated by a connecting line) with `TUT_TERR_GAR_CT`, likely a many-to-one relationship where multiple policy sums can be associated with one territorial guarantee code.

* **TUT\_GEOLOCALIZZAZIONE:** This table likely stores geolocation information.
    * `COD_CONTRATTO`: VARCHAR (Contract Code)
    * `COD_COMPON`: VARCHAR (Component Code)
    * `TMS_INSERIMENTO`: TIMESTAMP (Insertion Timestamp - likely part of the primary key or used for tracking)
    * **Relationships:**
        * No direct relationships to the other main policy tables are explicitly shown with connecting lines in this view. However, the field names `COD_CONTRATTO` and `COD_COMPON` suggest a potential link to policy information.

* **OSP.TLT\_GPERS\_CAT\_TRAS\_RT\_OC:** The table name suggests it stores information related to insured persons, catastrophe types, transport types, risk types, and occupation codes. The fields are not visible in the screenshot.
    * **Relationships:**
        * Has a relationship (indicated by a connecting line) with `TPA_RADICE`, though the specifics aren't detailed in terms of foreign keys in this view.

* **TLT\_ITBTABEL:** The table name suggests it stores various types of reference data. The fields are not visible in the screenshot.
    * **Relationships:**
        * No direct relationships to the other main policy tables are explicitly shown with connecting lines in this view.

* **TUT\_TERRITORIO:** This table likely stores territorial information.
    * `PROGR`: INT (Progressive Number - likely the primary key)
    * `SIGLA_PROVINCIA`: VARCHAR (Province Abbreviation)
    * `COD_BELIORE`: VARCHAR (Belgiore Code - likely a specific geographic code)
    * `COD_REGIONE`: VARCHAR (Region Code)
    * `COD_BELPU_COMUNE`: VARCHAR (Belpu Municipality Code - likely a specific geographic code)
    * `COD_PROVINCIA`: VARCHAR (Province Code)
    * `COD_COMUNE`: VARCHAR (Municipality Code)
    * `CAP`: VARCHAR (Postal Code)
    * `SIGLA_PRO_TARGA`: VARCHAR (License Plate Province Abbreviation)
    * `COD_STAT_PREF`: VARCHAR (Prefecture State Code)
    * `CAP_PREC`: VARCHAR (Previous Postal Code)
    * `CODICE_ISTAT`: VARCHAR (ISTAT Code - Italian National Institute of Statistics code)
    * `CODICE_ISO`: VARCHAR (ISO Code)
    * `DATA_CREAZIONE`: DATE (Creation Date)
    * `INFO_PRINC`: VARCHAR (Principal Information)
    * `TMS_ULT_EDIT`: TIMESTAMP (Last Edit Timestamp)
    * `UTENTE_EDIT`: VARCHAR (User who edited)
    * `DESCRIZIONE_ESTERA`: VARCHAR (Foreign Description)
    * **Relationships:**
        * Has a relationship (indicated by a connecting line) with `TUT_TERR_GAR_CT`, likely a one-to-many relationship where one territory can be associated with multiple territorial guarantee codes.

* **TUT\_TERR\_GAR\_CT:** This table likely links territories to specific guarantee codes.
    * `PROGR`: INT (Progressive Number - likely part of the primary key)
    * `COD_GARANZIA`: VARCHAR (Guarantee Code - likely part of the primary key)
    * **Relationships:**
        * Has a relationship (indicated by a connecting line) with `TUT_TERRITORIO`, likely a many-to-one relationship where multiple territorial guarantee codes can be associated with one territory.
        * Has a relationship (indicated by a connecting line) with `TPT_SOMMA`, likely a many-to-one relationship where multiple policy sums can be associated with one territorial guarantee code.

This diagram provides a high-level view of the key entities and their relationships within the insurance policy processing system's database schema in DB2. It highlights how policy information is structured and linked to related data such as installments, sums insured, factors, and geographical information.

### 5.3 Data Dictionary

The policy processing system uses various fields and data structures to represent policy information. The critical fields and data structures include:

* NUM-POLIZZA: The policy number, a unique identifier for each policy.
* COD-COMPON: The component code, which identifies a specific component within a policy.
* TMS-INSERIMENTO: The insertion timestamp, which records when a record was created.
* REVKEY: The revision key, which tracks changes to a record.
* REVKEY-SUB: The sub-revision key, which tracks changes within a specific component of a record.
* DATA-INIZ-COMPET: The competence start date, which indicates when a policy or policy component takes effect.
* DATA-FINE-COMPET: The competence end date, which indicates when a policy or policy component expires.
* STATO: The status of a policy or policy component, such as active, canceled, or expired.
* SUMA-ASSICURATA: The sum insured, which represents the maximum amount the insurer will pay in case of loss.
* PREMIO: The premium, which is the amount the insured pays for the insurance coverage.
* FRANCHIGIA: The deductible, which is the amount the insured must pay out of pocket before the insurer begins to cover losses.
* CLASSE-RISCHIO: The risk class, which represents the level of risk associated with a policy.
* CODICE-VALUTA: The currency code, which indicates the currency in which a policy is issued.
* TIPO-AGENZIA: The agency type, which indicates whether an agency is a main branch or a subsidiary.
* CODICE-GARANZIA: The guarantee code, which identifies a specific type of insurance coverage.
* CLASSE-TERRITORIALE: The territorial class, which represents the risk associated with a specific geographic location.

These fields and data structures are used throughout the system to capture, process, and store policy information. They are essential to the system's functionality and for ensuring the accuracy and integrity of policy data.

## 6. Technical Components

### 6.1 Data Access Modules

The policy processing system uses various data access modules to interact with the databases. These modules encapsulate the data access logic, providing a consistent interface for accessing data from different sources. The key data access modules include:

* ELSRQ014: This module retrieves data from the root segment of a technical database based on input criteria.
* EDLRFU3A: This module retrieves data from the TPT\_SOMMA\_FATTORE table based on different access methods.
* EDLR1F05: This module accesses an administrative database to retrieve policy information, specifically the policy's company code.
* EDLRWF79: This module retrieves a geolocation record from the TUT\_GEOLOCALIZZAZIONE table based on provided contract code, component code, and insertion timestamp.
* EDLRUF44: This module retrieves data from the OSP.TLT\_GPERS\_CAT\_TRAS\_RT\_OC table based on various input criteria.
* EDLRTF52: This module reads data from a table named TPT\_SOMMA in a DB2 database. It supports random access based on a key and sequential access using a cursor.
* PLSYUT16: This module reads a record from a database table based on a provided key.
* ELSBPAG5: This module processes insurance transactions in batch, retrieves data from a database, and formats it for output.

These modules use a combination of embedded SQL statements and DL/I calls to interact with the databases. They handle tasks such as connecting to the database, executing queries, retrieving data, and handling errors. The encapsulation of data access logic in these modules promotes code reuse and facilitates maintenance and enhancements.

### 6.2 Date and Time Utilities

The policy processing system uses various date and time utilities to manipulate dates and timestamps. These utilities provide functions for validating dates, calculating date differences, generating timestamps, and converting dates between different formats. The key date and time utilities include:

* IYYCRDA8: This utility validates a date in 'YYMMDD' format.
* PLSYUT35: This utility generates a timestamp by combining the current date and time.
* PLSYUT36: This utility decodes a timestamp into its component parts: year, month, day, hour, minute, second, and hundredth of a second.
* PLSYUT68: This utility decodes an 8-byte internal timestamp to a 26-byte external timestamp for DB2.
* PLSYUT74: This utility determines whether a year is a leap year.
* PLSYUT37: This utility calculates the difference in business days between two dates.

These utilities are used throughout the system to ensure the accuracy and consistency of date and time data. They are essential for tasks such as premium calculation, policy expiration date management, and report generation.

### 6.3 Calculation Functions

The policy processing system uses various calculation functions to perform mathematical and financial calculations. These functions are used to calculate premiums, deductibles, currency conversions, and other policy-related values. The key calculation functions include:

* EGERVL01: This function determines exchange rates between the Italian lira and other currencies.
* EGERVL03: This function handles currency conversions and calculations.
* KRPD0077: This function calculates the risk class of the main risk of an insurance policy.
* KRPD0339: This function calculates the company code and centralized code based on an environment flag.
* KRPD0418: This function retrieves rates, deductibles, limits, and territorial classes based on location and insurance policy details.
* KRPM1112: This function retrieves information about a location (comune) from the TUT\_TERRITORIO table based on provided location name, postal code, and province.
* PLSYUTG0: This function rounds a number to a specific number of decimals based on the currency code.
* PLSYUTG2: This function rounds a number to a specific number of decimals (0 to 3).

These functions use a combination of formulas, lookup tables, and business rules to perform the necessary calculations. They are essential for the accuracy and consistency of the system's financial data.

### 6.4 Error Management

The policy processing system implements error management mechanisms to handle errors and exceptions that can occur during policy processing. These mechanisms ensure that the system can recover from errors and continue operating correctly. The key error management mechanisms include:

* SQLCODE Handling: The system checks the SQLCODE after each database operation. If the SQLCODE indicates an error, the system takes appropriate action, such as logging the error, displaying an error message, or abnormally terminating the program.
* Abnormal Termination Handling: The system uses an abnormal termination routine to handle unexpected situations, such as severe database errors or program errors. The abnormal termination routine logs the error, generates a system dump, and terminates the program.
* Error Logging: The system logs all errors to an error log file. This provides a record of errors that can be used for debugging and troubleshooting.
* Error Messages: The system displays error messages to the user in case of errors. These messages provide information about the error and how to resolve it.

The error management mechanisms are designed to be comprehensive and robust, ensuring that the system can handle a wide range of potential errors. This helps maintain the integrity of the system's data and ensure that the system continues to function correctly.

## 7. Integrations

### 7.1 External Systems

The policy processing system integrates with various external systems to exchange data and functionality. These external systems include:

- Underwriting Systems: The system integrates with underwriting systems to retrieve information about underwriting, such as rates and underwriting rules.
- Billing Systems: The system integrates with billing systems to generate invoices and process payments.
- Claims Systems: The system integrates with claims systems to provide policy data for claims processing.
- Reporting Systems: The system integrates with reporting systems to provide data for report generation.

Integrations with external systems are accomplished using a variety of methods, including batch files, file transfers, and APIs. The system is designed to be flexible and adaptable, allowing for integration with new systems as needed.

### 7.2 Data Interfaces

The policy processing system uses various data formats and protocols to exchange information with external systems. These interfaces ensure that data can be exchanged accurately and efficiently. The data interfaces used by the system include:

- Batch Files: Batch files are used to exchange data with external systems in a batch processing mode. These files typically contain large volumes of data and are processed periodically.
- File Transfers: File transfers are used to exchange data with external systems using file transfer protocols, such as FTP.
- APIs: APIs (Application Programming Interfaces) are used to exchange data with external systems in real-time. APIs allow systems to communicate directly with each other, exchanging data and functionality.
- Message Queues: Message queues are used to exchange data asynchronously between systems. Messages are placed in a queue and processed by the receiving system when it is available.

The system is designed to support a variety of data formats, including fixed-length records, comma-separated values (CSV), and XML. This ensures that the system can exchange data with a wide range of external systems.

## 8. Glossary

This glossary provides definitions for technical terms and acronyms used in this document.

- **ABEND**: Abnormal termination of a program.
- **COBOL**: Common Business-Oriented Language, a programming language.
- **Copybook**: A file containing COBOL data definitions that can be included in other programs.
- **Cursor**: A database mechanism that allows a program to process a set of records one at a time.
- **DB2**: A relational database management system.
- **DL/I**: Data Language/I, a data access language used to interact with IMS databases.
- **IMS**: Information Management System, a hierarchical database management system.
- **JCL**: Job Control Language, a language used to control the execution of batch jobs on mainframe systems.
- **PCB**: Program Communication Block, a data structure used to communicate with an IMS database.
- **Premium**: The amount an insured pays for insurance coverage.
- **Sum Insured**: The maximum amount an insurer will pay in case of loss.
- **Deductible**: The amount an insured must pay out of pocket before the insurer begins to cover losses.
- **Risk Class**: A classification that represents the level of risk associated with an insured or policy.
- **Coinsurance**: An arrangement where multiple insurers share the risk of a policy.
- **Catastrophe Modeling**: The process of using computer models to estimate potential losses from catastrophic events.
- **Currency onversion**: The process of converting amounts from one currency to another.
- **Territorial Class**: A classification that represents the risk associated with a specific geographic location.
- **Guarantee Code**: A code that identifies a specific type of insurance coverage.
- **Mainframe**: A large, powerful computer that is typically used in large organizations for critical applications.

## 9. Appendix

### 9.1 Detailed functions descriptions (Sample of only one function, this can be replicated for each one)

**KRPD0077: Determining the Main Risk Class of an Insurance Policy**

The KRPD0077 COBOL program is a crucial component within a larger insurance system, responsible for determining the risk class associated with the main risk of a given insurance policy. This risk class is essential for various downstream processes, including premium calculation, risk assessment, and reporting.

**How KRPD0077 Works:**

1. **Initialization**: The program begins by initializing its working storage variables and setting up the environment for execution.
2. **Data Retrieval**: 
    - Policy Information: The program retrieves essential policy information using then ELSRQ001 external program. This information likely includes the policy number, policy branch code (D0077-CODICE-RAMO), and effective date (MS01-DATA-COMPETENZA).
    - Premium Details: The program then retrieves premium details associated with the policy using the ELSRQ130 external program. This data likely includes details about different premium components, their accounting classes, and imponible premium amounts.
3. **Premium Processing and Categorization**:
    - Rate Code Check: The program checks the policy's rate code. If the rate code is 'U', it processes premiums directly associated with the policy. Otherwise, it processes premiums associated with the policy's installments.
    - Balance Branch Determination: For each premium record, the program determines the balance branch using the 0200-VALORIZZA-RAMO-BILANCIO section. This section likely uses the premium's accounting class and branch code to map it to a specific balance branch.
    - Premium Categorization: Based on the balance branch, the program categorizes premiums into two tables:
        - Main Premium Table: Stores premiums where the balance branch matches the policy branch code (D0077-CODICE-RAMO)
        - Secondary Premium Table: Stores premiums where the balance branch is different from the policy branch code.
4. **Risk Identification**:
    - Highest Imponible Premium: The program aims to identify the risk with the highest imponible premium. It follows a prioritized approach:
        - Main Table Priority: If the main premium table is not empty, it searches for the risk with the highest imponible premium within this table.
        - Secondary Table with Exclusion: If the main table is empty, it searches for the risk with the highest imponible premium in the secondary table, excluding risks with a balance branch of '3R'. This exclusion suggests a business rule where risks with balance branch '3R' are considered less significant unless they are the only options.
        - Secondary Table Inclusion: If no risk is found in the secondary table with the exclusion, the program searches again, this time including all risks in the secondary table.
5. **Return Results**:
    - The program returns the risk type (D0077-TIPO-RISCHIO) and risk class (D0077-CLASSE-RISCHIO) associated with the identified risk with the highest imponible premium. It also returns a RETURN-CODE indicating the success or failure of the program's execution.

KRPD0077                           ELSRQ001     ELSRQ130     0200-VALORIZZA-RAMO-BILANCIO
    |                                  |            |                 |
    | Get Policy Information           |            |                 |
    | (Policy Number, Branch Code,     |            |                 |
    | Effective Date)                  |            |                 |
    |--------------------------------->|            |                 |
    |                                  |            |                 |
    | Return Policy Information        |            |                 |
    |<---------------------------------|            |                 |
    |                                  |            |                 |
    | Get Premium Details              |            |                 |
    | (Policy Number, Effective Date)  |            |                 |
    |--------------------------------->|            |                 |
    |                                  |            |                 |
    | Return Premium Details           |            |                 |
    |<---------------------------------|            |                 |
    |                                  |            |                 |
    |-loop [For Each Premium Record]----------------------------------|
    |   |                              |            |                 |
    |   | Determine Balance Branch     |            |                 |
    |   | (Accounting Class, Branch Code)           |                 |
    |   |------------------------------------------------------>|     |
    |   |                              |            |          |     |
    |   | Return Balance Branch        |            |          |     |
    |   |<------------------------------------------------------|     |
    |   |                              |            |                 |
    |   |-alt [Balance Branch = Policy Branch]                        |
    |   |   |                          |            |                 |
    |   |   | Store Premium in Main Table            |                 |
    |   |   |                          |            |                 |
    |   |   |                          |            |                 |
    |   | [Balance Branch != Policy Branch]          |                 |
    |   |   |                          |            |                 |
    |   |   | Store Premium in Secondary Table       |                 |
    |   |   |                          |            |                 |
    |   |   |                          |            |                 |
    |   |                              |            |                 |
    |                                  |            |                 |
    |-alt [Main Premium Table is Not Empty]          |                 |
    |   |                              |            |                 |
    |   | Find Risk with Highest Imponible Premium in Main Table      |
    |   |                              |            |                 |
    |   |                              |            |                 |
    | [Main Premium Table is Empty]    |            |                 |
    |   |                              |            |                 |
    |   |-alt [Exclude Balance Branch '3R']          |                 |
    |   |   |                          |            |                 |
    |   |   | Find Risk with Highest Imponible Premium in Secondary Table (excluding '3R') |
    |   |   |                          |            |                 |
    |   |   |                          |            |                 |
    |   | [No Risk Found]              |            |                 |
    |   |   |                          |            |                 |
    |   |   | Find Risk with Highest Imponible Premium in Secondary Table (including all) |
    |   |   |                          |            |                 |
    |   |   |                          |            |                 |
    |   |                              |            |                 |
    |                                  |            |                 |
    | Return Risk Type, Risk Class, and Return Code  |                 |
    |---------------------------------------------------------------->|
    |                                  |            |                 |
KRPD0077                           ELSRQ001     ELSRQ130     0200-VALORIZZA-RAMO-BILANCIO

This sequence diagram visually represents the flow of logic within KRPD0077, highlighting the interactions with external programs and the decision-making process for identifying the main risk class.