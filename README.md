# BIF601 Programming Essentials Final Project 
# ELISA Analysis in Python

Application filename: 'log4pl_ELISA_v1.0.py'

## Background

Enzyme-linked immunosorbent assay (ELISA) is a laboratory technique which uses an enzyme-bound antibody or antigen to detect and measure presence of antibodies, antigens, and proteins in biological samples such as blood, urine, or saliva. ELISA has continued to be proven to be a standard analytical tool in science and industry since its development in the 1960s as this method detects and measures tiny amounts of analytes with high accuracy and precision (Lequin, 2005). 

Raw data from ELISA often requires a prior adaptation using proprietary software or exporting the results into external internet platforms (Danielak et al., 2020). 

## Description

This is an ELISA Tool as an application to analyze data generated from ELISA. The application will allow users to input generated data, for example, concentration (x) and absorbance results (y) and use libraries such as NumPy, SciPy, Matplotlib, and Pandas for data processing and analysis. The application will use the ‘curve_fit’ function in SciPy to fit a 4-parameter logistic regression model to the input data. The data and visualization of the predicted model are built using functions from the Matplotlib library and will present a sigmoid curve.

After the graph is presented, the application will provide an option for the user to input measured absorbance results and use the modeled function to interpolate the unknown concentration as output. 

A final report will be generated summarizeing all the results and date stamped for good laboratory practices. A second output uses the Plotly graphing library to present an interactive graph, improving data analysis.

## Target end user

Research and production laboratories that produce ELISA results.

## Technologies
Project is created with:
* Spyder version: 5.4.3  (conda)
* Python version: 3.11.5 64-bit
* Qt version: 5.15.2
* PyQt5 version: 5.15.7
* Operating System: Windows 10

## Examples of use

![image1](https://github.com/b-shen/BIF601_final_project/blob/main/images/image1.png?raw=true)

![image2](https://github.com/b-shen/BIF601_final_project/blob/main/images/image2.png?raw=true)

![image3](https://github.com/b-shen/BIF601_final_project/blob/main/images/image3.png?raw=true)

## Sources
Lequin, R. M. (2005). Enzyme Immunoassay (EIA)/Enzyme-Linked Immunosorbent Assay (ELISA). Clinical Chemistry, 51(12), 2415–2418. https://doi.org/10.1373/clinchem.2005.051532.

Danielak, D., Banach, G., Walaszczyk, J., Romański, M., Bawiec, M. A., Paszkowska, J., Zielińska, M., Sczodrok, J., Wiater, M., Hoc, D., Kołodziej, B., & Garbacz, G. (2020). A novel open source tool for ELISA result analysis. Journal of Pharmaceutical and Biomedical Analysis, 189, 113415. https://doi.org/10.1016/j.jpba.2020.113415.
