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
        self.ClientPhone = col2.text_input("Enter Client phone number")
        col1, col2 = st.columns(2)
        self.Jobsite = col1.text_input("Enter Job Address")
        self.InspectionDate = col2.date_input("Enter Inspection Date", format="MM/DD/YYYY")

        st.header("Roof Info")
        col1, col2 = st.columns(2)

        self.RoofType = col1.text_input("Enter Roof Type")
        self.Color = col2.text_input("Enter Roof Color")
        col1, col2 = st.columns(2)
        self.Stories = col1.number_input("Enter Number of Stories", value=0)
        self.Pitch = col2.text_input("Enter Roof Pitch")
        col1, col2 = st.columns(2)
        self.EstimatedAge = col1.number_input("Enter Estimated Roof Age", value=0)
        self.RemainingYears = col2.number_input("Enter Remaining Years", value=0)
        col1, col2 = st.columns(2)
        self.Leaks = col1.text_input("Enter number of Leaks Disclosed")
    
    def GatherAdditionalDamages(self) :
        # Collect Additional Damages (Call super after Declaring Title and Specific Damages in Child)
        col1, col2 = st.columns(2)
        self.Junctions = col1.number_input("Enter number of Damaged Junctions", value=0)
        self.RubberCollars = col2.number_input("Enter number of Damaged Rubber Collars", value=0)
        col1, col2 = st.columns(2)
        self.ChimneyFlashings = col1.number_input("Enter number of Damaged Chimney Flashings", value=0)
        self.RoofJackFlashings = col2.number_input("Enter number of Damaged Roof Jack Flashings", value=0)
        col1, col2 = st.columns(2)
        self.SidewallFlashings = col1.number_input("Enter number of Damaged Sidewall Flashings", value=0)
        self.DryRot = col2.text_input("Describe Dry Rot Damage Areas")
        self.AdditionalInfo = st.text_input("Additional Input:")
    
    def CollectPhotos(self) :
        Photos = {
            "Junctions" : st.file_uploader("Upload Photos of Damaged Junctions", type=["jpg", "png", "jpeg"], accept_multiple_files=True),
            "Rubber Collars" : st.file_uploader("Upload Photos of Damaged Rubber Collars", type=["jpg", "png", "jpeg"], accept_multiple_files=True),
            "Flashings" : st.file_uploader("Upload Photos of Damaged/Dirty Chimney, Sidewall, Headwal or Roof Jack Flashings", type=["jpg", "png", "jpeg"], accept_multiple_files=True),
            "Valleys" : st.file_uploader("Upload Photos of Damaged/Dirty Valleys", type=["jpg", "png", "jpeg"], accept_multiple_files=True),
            "Dry Rot" : st.file_uploader("Upload Photos of Dry Rot Damage", type=["jpg", "png", "jpeg"], accept_multiple_files=True),
            "Home" : st.file_uploader("Upload Home Photos", type=["jpg", "png", "jpeg"], accept_multiple_files=True),
            "Additional" : st.file_uploader("Upload Any Additional Photos Photos", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
        }

        return Photos
        
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
        st.markdown(f'<button kind="secondary" class="css-7ym5gk ef3psqc11"><div data-testid="stMarkdownContainer" class="css-1vbkxwb e1nzilvr4"><a style="text-decoration: none; color: inherit;" href="data:text/html;base64,{base64.b64encode(html.encode()).decode()}" target="_blank">Open Assembled HTML</a></div></button>', unsafe_allow_html=True)

class TileInspection(Report) :
    def __init__(self):
        super().__init__()
        self.GatherAdditionalDamages()
        # self.CollectPhotos()

    def GatherAdditionalDamages(self):
        # Title and Columns
        st.header("Roof Damages")
        col1, col2 = st.columns(2)

        # Tile Specific Inputs
        self.BrokenTiles = col1.number_input("Enter number of Broken Tiles", value=0)
        self.DamagedTiles = col2.number_input("Enter number of Damaged Tiles", value=0)
        col1, col2 = st.columns(2)
        self.BrokenRidgeRaketiles = col1.number_input("Enter number of Broken Ridge or Rake Tiles", value=0)
        self.SlippedTiles = col2.number_input("Enter number of Slipped Tile Areas", value=0)
        super().GatherAdditionalDamages()


    def CollectPhotos(self):
        st.header("Add Photos")

        self.Photos = {
            "Shingles" : st.file_uploader("Upload Photos of Broken/Damaged Tiles", type=["jpg", "png", "jpeg"], accept_multiple_files=True),
        }
        AdditionalPhotos = super().CollectPhotos()

        self.Photos.update(AdditionalPhotos)
        
class CompInspection(Report) :
    def __init__(self):
        super().__init__()
        self.GatherAdditionalDamages()
        self.CollectPhotos()
    
    def GatherAdditionalDamages(self):
        # Title and Columns
        st.header("Roof Damages")
        col1, col2 = st.columns(2)

        # Tile Specific Inputs
        self.BrokenTiles = col1.number_input("Enter number of Damaged Shingles", value=0)
        self.DamagedHips = col2.number_input("Enter number of Damaged Hips", value=0)
        self.DamagedRidges = col1.number_input("Enter number of Damaged Ridges", value=0)
        super().GatherAdditionalDamages()
    
    def CollectPhotos(self):
        st.header("Add Photos")

        self.Photos = {
            "Shingles" : st.file_uploader("Upload Photos of Damaged Shingles", type=["jpg", "png", "jpeg"], accept_multiple_files=True),
            "Ridges" : st.file_uploader("Upload Photos of Damaged Hips/Ridges", type=["jpg", "png", "jpeg"], accept_multiple_files=True)
        }

        AdditionalPhotos = super().CollectPhotos()

        self.Photos.update(AdditionalPhotos)

    

        

def main() :
    st.header("Triark Swift Reports")
    # oReport = TileInspection()
    # if st.button("Create Page") :
    #         oReport.GeneratePage()
    genre = st.radio("Select Report Type:", ('Tile', 'Composition'))

    if genre == 'Tile':
        oReport = TileInspection()
        if st.button("Create Page") :
                oReport.GeneratePage()
    elif genre == 'Composition':
        oReport = CompInspection()
        if st.button("Create Page") :
                oReport.GeneratePage()
    else:
        st.write('Please select a Report Type')
        
    

if __name__ == "__main__":
    main()
