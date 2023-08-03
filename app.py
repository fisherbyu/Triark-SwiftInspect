import streamlit as st
import base64

class Report() :
    # Define Static Attributes
    Company = "Triark Roofing"
    CompanyAddressL1 = "951 Washington Blvd"
    CompanyAddressL2 = "Suite 519"
    CompanyAddressCity = "Roseville, CA"
    Phone = "(916) 276-8632"
    Email = "triarkroofing@gmail.com"

    # Construct and Add in Dynamic Attributes
    def __init__(self):
        st.header("Client Info")
        col1, col2 = st.columns(2)

        self.ClientName = col1.text_input("Enter Client's Name")
        self.ClientPhone = col1.text_input("Enter Client phone number")
        self.Jobsite = col2.text_input("Enter Job Address")
        self.InspectionDate = col2.date_input("Enter Inspection Date")

        st.header("Roof Info")
        col1, col2 = st.columns(2)

        self.RoofType = col1.text_input("Enter Roof Type")
        self.Color = col2.text_input("Enter Roof Color")
        self.Stories = col1.number_input("Enter Number of Stories", value=0)
        self.Pitch = col2.text_input("Enter Roof Pitch")
        self.EstimatedAge = col1.number_input("Enter Estimated Roof Age", value=0)
        self.RemainingYears = col2.number_input("Enter Remaining Years", value=0)
        self.Leaks = col1.text_input("Enter number of Leaks Disclosed")
        
    def assembleHTML(self, filepath):
        # Read in HTML String
        with open(filepath, "r", encoding="utf-8") as file:
            html_string = file.read()
        # Fill HTML with values
        for key, value in vars(self).items():
            placeholder = f"{{{{ {key} }}}}"  # Assuming dynamic values are represented as {{ variable_name }} in the HTML file.
            html_string = html_string.replace(placeholder, str(value))

        return html_string
    
    def GeneratePage(self) :
        html = html = self.assembleHTML("documents/html/base.html")
        st.markdown(f'<button kind="secondary" class="css-7ym5gk ef3psqc11"><div data-testid="stMarkdownContainer" class="css-1vbkxwb e1nzilvr4"><a href="data:text/html;base64,{base64.b64encode(html.encode()).decode()}" target="_blank">Open Assembled HTML</a></div></button>', unsafe_allow_html=True)
        

class TileInspection(Report) :
    def __init__(self):
        super().__init__()
        st.header("Roof Damages")
        col1, col2 = st.columns(2)
        self.BrokenTiles = col1.number_input("Enter number of Broken Tiles", value=0)
        self.DamagedTiles = col2.number_input("Enter number of Damaged Tiles", value=0)
        self.BrokenRidgeRaketiles = col1.number_input("Enter number of Broken Ridge or Rake Tiles", value=0)
        self.SlippedTiles = col2.number_input("Enter number of Slipped Tile Areas", value=0)
        self.Junctions = col1.number_input("Enter number of Damaged Junctions", value=0)
        self.RubberCollars = col2.number_input("Enter number of Damaged Rubber Collars", value=0)
        self.ChimneyFlashings = col1.number_input("Enter number of Damaged Chimney Flashings", value=0)
        self.RoofJackFlashings = col2.number_input("Enter number of Damaged Roof Jack Flashings", value=0)
        self.SidewallFlashings = col1.number_input("Enter number of Damaged Sidewall Flashings", value=0)
        self.DryRot = col2.text_input("Describe Dry Rot Damage Areas")
        self.AdditionalInfo = col1.text_input("Additional Input:")

def main() :
    oReport = TileInspection()
    
    if st.button("Create Page") :
        oReport.GeneratePage()

if __name__ == "__main__":
    main()
