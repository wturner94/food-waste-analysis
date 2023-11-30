# food-waste-analysis
<img src="https://www.barkerbrettell.co.uk/content/uploads/2022/09/foodrecycling.jpg" alt="food-waste image" width="627" height="418">

## ***about***
In this analysis, we delve into the multifaceted issue of food waste worldwide.
Our focus pits food waste against three dimensions: **food insecurity**, **economic wealth**, and **population density**.
In the interest of time, the scope of this analysis will be limited to the year 2020, providing us a snapshot of the complex interplay between these concepts that is likely close to what it would look like on December 1, 2023. 

## ***datasets used***
- Food waste by country (.CSV from Kaggle): https://www.kaggle.com/datasets/joebeachcapital/food-waste/data

- GDP per capita (wealth) by country (.CSV from Data.WorldBank.Org): https://data.worldbank.org/indicator/NY.GDP.PCAP.CD

- Population density by country (.CSV from Data.WorldBank.Org): https://data.worldbank.org/indicator/EN.POP.DNST

- Prevalence of moderate-to-severe food insecurity in the population by country (.CSV from Data.WorldBank.Org): https://data.worldbank.org/indicator/SN.ITK.MSFI.ZS?view=chart


## ***before you begin***
Check to see if your machine has met the following requirements:

- Installed Python. This project was developed using Python 3.11.6. If you don't have Python installed or if you need to upgrade your current version, you can download it from the [official Python website](https://www.python.org/downloads/).
- Installed Git, which is necessary to clone the repository. If you don't have Git installed, you can download it from the [official Git website](https://git-scm.com/downloads).

Follow these steps to run the project on your local machine:

1. **cloning the repository**

   Navigate to the directory where you want the cloned repository to be placed by using the ```cd``` command in your terminal followed by the path of the directory.
   
   Then you can clone this repository by running the following command in your terminal:

   ```
   git clone https://github.com/wturner94/food-waste-analysis.git
   ```
  
3. **navigating to the cloned directory**

   Change your current directory to the cloned repository's directory **food-waste-analysis**.

4. **establishing a virtual environment**

   It's recommended to create a virtual environment to keep the project's dependencies isolated from your system's Python environment. You can create a virtual environment using the following command:

   On Windows:

   ```
   python -m venv venv
   ```

   On macOS and Linux:

   ```
   python3 -m venv venv
   ```

   This will create a new virtual environment named `venv` in your current directory.

4. **activating the virtual environment**

   Activate the virtual environment using the following command:

   On Windows:

   ```
   .\venv\Scripts\activate
   ```

   On macOS and Linux:

   ```
   source venv/bin/activate
   ```

   Your prompt should change to indicate that you are now operating within a Python virtual environment. 

5. **installing the required packages**

   Install the required packages by running the following command:

   ```
   pip install -r requirements.txt
   ```

   You're now ready to run the project!

6. **running the ```food-waste-analysis.ipynb``` file:**
    - If you have Jupyter Notebook installed, enter ```jupyter notebook``` and open the `.ipynb` file.
    - If you are using Visual Studio Code, open the `.ipynb` file and select "Install" when asked "Do you want to install the recommended 'Python' extension from Microsoft for the Python Language?"
    - Attempt to "Run" the first code block by selecting the Run/Play button at the top left of the code block. This will prompt you to "Install/Enable the suggested extensions "Python" + "Jupyter"
    - Continue to run the cells using the Run/Play button that appears at the top left of each cell.

To deactivate the virtual environment when you're done, simply type `deactivate` in your terminal.