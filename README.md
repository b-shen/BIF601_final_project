# BIF601 Programming Essentials Final Project 
## ELISA Analysis in Python
### Background

Enzyme-linked immunosorbent assay (ELISA) is a laboratory technique which uses an enzyme-bound antibody or antigen to detect and measure presence of antibodies, antigens, and proteins in biological samples such as blood, urine, or saliva. ELISA has continued to be proven to be a standard analytical tool in science and industry since its development in the 1960s as this method detects and measures tiny amounts of analytes with high accuracy and precision (Lequin, 2005).
Raw data from ELISA often requires a prior adaptation using proprietary software or exporting the results into external internet platforms (Danielak et al., 2020). I want to develop an ELISA Tool as an application to analyze data generated from ELISA. The application will allow users to input generated data, for example, concentration (x) and absorbance results (y) and use libraries such as NumPy, SciPy, Matplotlib, and Pandas for data processing and analysis. The application will use the ‘curve_fit’ function in SciPy to fit a 4-parameter logistic regression model to the input data. The data and visualization of the predicted model are built using functions from the Matplotlib library and will present a sigmoid curve.
After the graph is presented, the application will provide an option for the user to input measured absorbance results and use the modeled function to interpolate the unknown concentration as output. A second output uses the Plotly graphing library to present an interactive graph, improving data analysis.

### References
Lequin, R. M. (2005). Enzyme Immunoassay (EIA)/Enzyme-Linked Immunosorbent Assay (ELISA). Clinical Chemistry, 51(12), 2415–2418. https://doi.org/10.1373/clinchem.2005.051532.
