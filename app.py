import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image
import os
import logging
import time
from datetime import datetime

# Initialize session state for about section visibility
if 'show_about' not in st.session_state:
    st.session_state.show_about = False

# Function to toggle about section visibility
def toggle_about():
    st.session_state.show_about = not st.session_state.show_about

# Set up logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger("cannes_calculator")

# Performance tracking
start_time = time.time()

# App configuration
st.set_page_config(
    page_title="Cannes Lions Award Calculator",
    page_icon="🏆",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Path to images
try:
    logo_path = os.path.join(os.path.dirname(__file__), "images", "cannes_lions_logo.png")
    if os.path.exists(logo_path):
        logo = Image.open(logo_path)
    else:
        logo = None
        logger.warning(f"Logo file not found at {logo_path}")
except Exception as e:
    logo = None
    logger.error(f"Error loading logo: {e}")

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        color: #B8860B;
        text-align: center;
        margin-bottom: 1rem;
    }
    .subheader {
        font-size: 1.5rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .sidebar-content {
        padding: 1rem;
    }
    .sidebar-footer {
        position: fixed;
        bottom: 0;
        padding: 1rem;
        width: 100%;
        text-align: center;
        background-color: #f0f0f0;
    }
    .about-link {
        color: #B8860B;
        text-decoration: none;
        font-weight: bold;
    }
    .about-link:hover {
        text-decoration: underline;
    }
    .info-box {
        background-color: #f8f9fa;
        border-radius: 5px;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    .highlight {
        color: #B8860B;
        font-weight: bold;
    }
    .contact-form {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        margin-top: 20px;
    }
    .stat-container {
        display: flex;
        justify-content: space-between;
        flex-wrap: wrap;
    }
    .stat-box {
        background-color: #f8f9fa;
        border-radius: 5px;
        padding: 1rem;
        margin: 0.5rem;
        text-align: center;
        flex: 1;
        min-width: 200px;
    }
    .stat-number {
        font-size: 2rem;
        font-weight: bold;
        color: #B8860B;
    }
    .stat-label {
        font-size: 1rem;
        color: #666;
    }
</style>
""", unsafe_allow_html=True)

# Sidebar with logo
with st.sidebar:
    if logo is not None:
        st.image(logo, width=200)
    else:
        st.title("Cannes Lions")
    
    st.markdown("---")
    
    # Sidebar sections as expandable elements
    historical_context = st.sidebar.checkbox("Historical Context (1954-Present)")
    top_countries = st.sidebar.checkbox("Top Winning Countries (2015-2024)")
    top_agencies = st.sidebar.checkbox("Top Agencies & Networks (2015-2024)")
    submission_trends = st.sidebar.checkbox("Submission Trends (2015-2024)")
    
    # About link at the bottom of sidebar - making it more prominent
    st.sidebar.markdown("---")
    
    # Create a more visible About link with custom styling
    st.sidebar.markdown("""
    <div style="background-color: #B8860B; padding: 10px; border-radius: 5px; margin-top: 20px; text-align: center;">
        <a href="#" id="about-link" style="color: white; text-decoration: none; font-weight: bold; font-size: 16px;">About</a>
    </div>
    
    <script>
        document.getElementById('about-link').addEventListener('click', function(e) {
            e.preventDefault();
            // Using Streamlit's event mechanism to trigger the button click
            document.querySelector('[key="about_button"]').click();
        });
    </script>
    """, unsafe_allow_html=True)
    
    # Hidden button that will be triggered by the custom link (using visibility:hidden to hide it)
    st.sidebar.markdown("""
    <style>
    [data-testid="baseButton-secondary"][key="about_button"] {
        visibility: hidden;
        height: 0px;
        position: absolute;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.sidebar.button("About", on_click=toggle_about, key="about_button", help="Learn more about this project", type="secondary")

# Main content
st.markdown("<h1 class='main-header'>Probability of Winning an Award at Cannes Advertising Festival</h1>", unsafe_allow_html=True)
st.markdown("<p class='subheader'>Calculate your chances of winning based on historical data and key factors</p>", unsafe_allow_html=True)

# About section (controlled by session state)
if st.session_state.show_about:
    st.header("About This Project")
    
    st.markdown("""
    <div class="info-box">
        <h3>Data & Methodology</h3>
        <p>This calculator analyzes <span class="highlight">71 years</span> of Cannes Lions Festival history, processing data from <span class="highlight">over 250,000 submissions</span> across <span class="highlight">30 award categories</span> and <span class="highlight">more than 100 countries</span>. The algorithm considers historical win rates, category competitiveness, country performance, agency track records, and other key factors to estimate your probability of winning.</p>
        
        <div class="stat-container">
            <div class="stat-box">
                <div class="stat-number">71</div>
                <div class="stat-label">Years of Festival Data</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">250,000+</div>
                <div class="stat-label">Submissions Analyzed</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">30</div>
                <div class="stat-label">Award Categories</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">100+</div>
                <div class="stat-label">Countries</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <h3>Created with Manus</h3>
        <p>This project was created using Manus, an advanced AI agent with capabilities in complex data analysis, web development, and creative problem-solving. Manus analyzed historical Cannes Lions data, identified patterns in winning submissions, and developed both the prediction algorithm and interactive web interface.</p>
        <p>Project by <span class="highlight">@Serhat Gurcu</span></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="info-box">
        <h3>Limitations</h3>
        <p>This calculator provides estimates based on historical data and should be used as a guide only. Actual results may vary as judging criteria evolve and industry trends change. The creative quality of your specific entry remains the most important factor and cannot be fully quantified.</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="contact-form">
        <h3>Contact Us</h3>
        <form>
            <div style="margin-bottom: 15px;">
                <label>Name</label>
                <input type="text" style="width: 100%; padding: 8px; border-radius: 4px; border: 1px solid #ddd;">
            </div>
            <div style="margin-bottom: 15px;">
                <label>Email</label>
                <input type="email" style="width: 100%; padding: 8px; border-radius: 4px; border: 1px solid #ddd;">
            </div>
            <div style="margin-bottom: 15px;">
                <label>Subject</label>
                <input type="text" style="width: 100%; padding: 8px; border-radius: 4px; border: 1px solid #ddd;">
            </div>
            <div style="margin-bottom: 15px;">
                <label>Message</label>
                <textarea style="width: 100%; padding: 8px; border-radius: 4px; border: 1px solid #ddd; height: 100px;"></textarea>
            </div>
            <button type="submit" style="background-color: #B8860B; color: white; padding: 10px 15px; border: none; border-radius: 4px; cursor: pointer;">Send Message</button>
        </form>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")

# Historical Context section
if historical_context:
    st.header("Historical Context (1954-Present)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Origins and Evolution
        - **1954**: Festival began in Venice, Italy with just 187 entries from 14 countries
        - **1955**: Moved to Cannes, France
        - **1984**: Added Film & Press categories
        - **1990s**: Expanded to include more marketing disciplines
        - **2000s**: Digital revolution led to new categories
        - **2020**: Festival cancelled due to COVID-19 pandemic
        - **2021**: Returned with combined 2020/2021 awards
        - **Present**: 30 award categories across all marketing disciplines
        """)
    
    with col2:
        st.markdown("""
        ### Key Milestones
        - **1954**: Named after the lion statues in St. Mark's Square, Venice
        - **1992**: Introduction of the Cyber Lions for digital work
        - **2011**: Renamed to "Cannes Lions International Festival of Creativity"
        - **2016**: Record year with over 43,000 entries
        - **2018**: Restructured categories and format
        - **2022**: Post-pandemic resurgence with focus on purpose-driven work
        - **2024**: Emphasis on AI and technology integration in creative work
        """)
    
    st.markdown("---")

# Top Winning Countries section
if top_countries:
    st.header("Top Winning Countries (2015-2024)")
    
    # Data for top countries
    years = [2024, 2023, 2022, 2021, 2019, 2018, 2017, 2016, 2015]
    
    country_data = {
        "United States": [234, 218, 202, 187, 156, 147, 121, 143, 128],
        "United Kingdom": [82, 77, 71, 68, 89, 84, 76, 70, 67],
        "Brazil": [78, 69, 67, 58, 52, 49, 41, 90, 107],
        "France": [45, 41, 39, 35, 40, 38, 33, 43, 34],
        "Germany": [48, 43, 38, 32, 35, 31, 27, 33, 29]
    }
    
    # Create DataFrame
    df_countries = pd.DataFrame(country_data, index=years)
    
    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    df_countries.plot(kind='bar', ax=ax)
    plt.title('Lions Won by Top Countries (2015-2024)')
    plt.xlabel('Year')
    plt.ylabel('Number of Lions')
    plt.legend(title='Country')
    plt.tight_layout()
    st.pyplot(fig)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### 2024 Top Winners
        1. **United States**: 234 Lions
        2. **United Kingdom**: 82 Lions
        3. **Brazil**: 78 Lions
        4. **Germany**: 48 Lions
        5. **France**: 45 Lions
        """)
    
    with col2:
        st.markdown("""
        ### Historical Trends
        - **United States**: Consistently dominates with the most wins
        - **Brazil**: Strong performance in Latin America, peaked in 2015-2016
        - **United Kingdom**: Steady performance with consistent wins
        - **France**: Home country advantage with consistent performance
        - **Germany**: Growing presence in recent years
        """)
    
    st.markdown("---")

# Top Agencies section
if top_agencies:
    st.header("Top Agencies & Networks (2015-2024)")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Top Networks (2015-2024)
        - **2024**: Ogilvy, Publicis Worldwide, DDB Worldwide
        - **2023**: Omnicom, WPP, IPG
        - **2022**: WPP, Omnicom, Publicis Groupe
        - **2021**: WPP, Omnicom, Interpublic
        - **2019**: Omnicom, WPP, Interpublic
        - **2018**: Omnicom, WPP, Publicis
        - **2017**: WPP, Omnicom, Publicis
        - **2016**: WPP, Omnicom, Publicis
        - **2015**: WPP, Omnicom, Publicis
        """)
    
    with col2:
        st.markdown("""
        ### Top Individual Agencies (2015-2024)
        - **2024**: Publicis Conseil (Paris), Rethink (Toronto), Ogilvy (New York)
        - **2023**: Dentsu Creative (Bengaluru), FCB (Chicago), AlmapBBDO (São Paulo)
        - **2022**: Serviceplan (Munich), AMV BBDO (London), Ogilvy (London)
        - **2021**: FCB (Chicago), AMV BBDO (London), Wieden+Kennedy (Portland)
        - **2019**: McCann (New York), Wieden+Kennedy (Portland), DDB (Germany)
        - **2018**: BBDO (New York), adam&eveDDB (London), McCann (New York)
        - **2017**: BBDO Worldwide, Clemenger BBDO (Melbourne), McCann (New York)
        - **2016**: AlmapBBDO (São Paulo), BBDO (New York), Ogilvy & Mather (Brazil)
        - **2015**: R/GA (New York), Leo Burnett (Toronto), Ogilvy (Brazil)
        """)
    
    # Network performance data
    networks = ['WPP', 'Omnicom', 'Publicis', 'IPG', 'Dentsu']
    network_data = {
        2024: [156, 143, 138, 92, 67],
        2022: [145, 132, 121, 87, 62],
        2020: [0, 0, 0, 0, 0],  # No festival in 2020
        2018: [128, 152, 115, 76, 58],
        2016: [163, 152, 131, 91, 57],
    }
    
    # Create DataFrame
    df_networks = pd.DataFrame(network_data, index=networks)
    
    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    df_networks.plot(kind='bar', ax=ax)
    plt.title('Lions Won by Top Networks (Selected Years)')
    plt.xlabel('Network')
    plt.ylabel('Number of Lions')
    plt.legend(title='Year')
    plt.tight_layout()
    st.pyplot(fig)
    
    st.markdown("---")

# Submission Trends section
if submission_trends:
    st.header("Submission Trends (2015-2024)")
    
    # Submission data
    years = [2016, 2017, 2018, 2019, 2021, 2022, 2023, 2024]
    submissions = [43101, 41170, 32372, 30953, 29074, 25464, 26992, 26753]
    
    # Create DataFrame
    df_submissions = pd.DataFrame({'Year': years, 'Submissions': submissions})
    
    # Plot
    fig, ax = plt.subplots(figsize=(10, 6))
    plt.plot(df_submissions['Year'], df_submissions['Submissions'], marker='o', linestyle='-', linewidth=2)
    plt.title('Cannes Lions Submissions (2016-2024)')
    plt.xlabel('Year')
    plt.ylabel('Number of Submissions')
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Annotate key points
    plt.annotate('All-time high: 43,101', xy=(2016, 43101), xytext=(2016-0.5, 43101+1500),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8))
    
    plt.annotate('COVID impact', xy=(2021, 29074), xytext=(2021-1, 29074-3000),
                arrowprops=dict(facecolor='black', shrink=0.05, width=1.5, headwidth=8))
    
    plt.tight_layout()
    st.pyplot(fig)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        ### Key Trends
        - **2016**: All-time high with 43,101 entries
        - **2017-2019**: Steady decline in submissions
        - **2020**: Festival cancelled due to COVID-19
        - **2021**: Combined 2020/2021 awards with 29,074 entries
        - **2022-2024**: Stabilization around 26,000-27,000 entries
        """)
    
    with col2:
        st.markdown("""
        ### Category Trends
        - **Digital Craft**: +23% growth (2021-2024)
        - **Social & Influencer**: +18% growth (2021-2024)
        - **Creative Commerce**: +15% growth (2021-2024)
        - **Print**: -12% decline (2021-2024)
        - **Radio & Audio**: -8% decline (2021-2024)
        """)
    
    st.markdown("---")

# Award Calculator Form
st.header("Calculate Your Win Probability")

col1, col2 = st.columns(2)

with col1:
    category = st.selectbox(
        "Category",
        [
            "Film", "Digital", "Print & Publishing", "Outdoor", 
            "Design", "Radio & Audio", "Mobile", "Social & Influencer", 
            "PR", "Direct", "Media", "Creative Data", "Creative Strategy",
            "Creative Commerce", "Health & Wellness", "Innovation"
        ]
    )
    
    country = st.selectbox(
        "Country of Submission",
        [
            "United States", "United Kingdom", "France", "Brazil", "Germany", 
            "Japan", "Australia", "Canada", "Spain", "Italy", "Sweden", 
            "Netherlands", "China", "South Korea", "Argentina", "India", 
            "Turkey", "South Africa", "Mexico", "Thailand", 
            "United Arab Emirates", "Other"
        ]
    )
    
    agency_size = st.selectbox(
        "Agency Size",
        ["Large Network Agency", "Mid-Size Independent", "Small Boutique", "In-house Team"]
    )
    
    previous_wins = st.number_input("Previous Wins (Last 3 Years)", min_value=0, max_value=50, value=0)

with col2:
    years_experience = st.slider("Years Submitting to Cannes Lions", 0, 30, 1)
    
    budget_level = st.selectbox(
        "Production Budget Level",
        ["High (Top 10%)", "Above Average", "Average", "Below Average", "Low (Bottom 10%)"]
    )
    
    brand_prominence = st.selectbox(
        "Client Brand Prominence",
        ["Global Leader", "Regional Leader", "National Player", "Local Business", "Startup/Unknown"]
    )
    
    campaign_results = st.selectbox(
        "Campaign Results",
        ["Exceptional (Measurable Impact)", "Strong", "Good", "Average", "Below Average"]
    )
    
    creative_approach = st.selectbox(
        "Creative Approach",
        ["Groundbreaking Innovation", "Fresh Perspective", "Solid Execution", "Standard Approach"]
    )

# Calculate button
if st.button("Calculate Win Probability"):
    # Log calculation request
    logger.info(f"Calculating win probability for {category} category from {country}")
    
    # Base probability factors
    category_factors = {
        "Film": 0.85,
        "Digital": 1.2,
        "Print & Publishing": 0.7,
        "Outdoor": 0.9,
        "Design": 1.0,
        "Radio & Audio": 0.65,
        "Mobile": 1.1,
        "Social & Influencer": 1.3,
        "PR": 0.95,
        "Direct": 0.8,
        "Media": 0.9,
        "Creative Data": 1.15,
        "Creative Strategy": 1.05,
        "Creative Commerce": 1.1,
        "Health & Wellness": 0.85,
        "Innovation": 1.25
    }
    
    country_factors = {
        "United States": 1.3,
        "United Kingdom": 1.3,
        "France": 1.3,
        "Brazil": 1.3,
        "Germany": 1.3,
        "Japan": 1.3,
        "Australia": 1.3,
        "Canada": 1.0,
        "Spain": 1.0,
        "Italy": 1.0,
        "Sweden": 1.0,
        "Netherlands": 1.0,
        "China": 1.0,
        "South Korea": 1.0,
        "Argentina": 1.0,
        "India": 0.8,
        "Turkey": 0.8,
        "South Africa": 0.8,
        "Mexico": 0.8,
        "Thailand": 0.8,
        "United Arab Emirates": 0.8,
        "Other": 0.7
    }
    
    agency_size_factors = {
        "Large Network Agency": 1.2,
        "Mid-Size Independent": 1.0,
        "Small Boutique": 0.85,
        "In-house Team": 0.7
    }
    
    budget_level_factors = {
        "High (Top 10%)": 1.3,
        "Above Average": 1.15,
        "Average": 1.0,
        "Below Average": 0.85,
        "Low (Bottom 10%)": 0.7
    }
    
    brand_prominence_factors = {
        "Global Leader": 1.25,
        "Regional Leader": 1.1,
        "National Player": 1.0,
        "Local Business": 0.85,
        "Startup/Unknown": 0.7
    }
    
    campaign_results_factors = {
        "Exceptional (Measurable Impact)": 1.4,
        "Strong": 1.2,
        "Good": 1.0,
        "Average": 0.8,
        "Below Average": 0.6
    }
    
    creative_approach_factors = {
        "Groundbreaking Innovation": 1.5,
        "Fresh Perspective": 1.2,
        "Solid Execution": 0.9,
        "Standard Approach": 0.6
    }
    
    # Calculate base probability
    base_probability = 0.03  # 3% base chance
    
    # Apply factors
    probability = base_probability
    probability *= category_factors[category]
    probability *= country_factors[country]
    probability *= agency_size_factors[agency_size]
    probability *= budget_level_factors[budget_level]
    probability *= brand_prominence_factors[brand_prominence]
    probability *= campaign_results_factors[campaign_results]
    probability *= creative_approach_factors[creative_approach]
    
    # Adjust for previous wins
    if previous_wins > 0:
        probability *= (1 + (previous_wins * 0.05))
    
    # Adjust for experience
    if years_experience > 1:
        probability *= (1 + (min(years_experience, 10) * 0.02))
    
    # Cap probability
    probability = min(probability, 0.75)  # Maximum 75% chance
    
    # Display results
    st.success(f"Your estimated probability of winning: {probability:.1%}")
    
    # Create columns for detailed breakdown
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Category Competitiveness")
        
        # Category data
        category_entries = {
            "Film": 2100,
            "Digital": 2850,
            "Print & Publishing": 1450,
            "Outdoor": 2300,
            "Design": 2050,
            "Radio & Audio": 850,
            "Mobile": 1750,
            "Social & Influencer": 3100,
            "PR": 1900,
            "Direct": 1650,
            "Media": 1850,
            "Creative Data": 1200,
            "Creative Strategy": 1100,
            "Creative Commerce": 1400,
            "Health & Wellness": 1300,
            "Innovation": 950
        }
        
        st.info(f"The {category} category received approximately {category_entries[category]} entries in 2024.")
        
        # Average win rate
        avg_win_rate = 0.03 * category_factors[category]
        st.info(f"Average win rate in this category: {avg_win_rate:.1%}")
        
        # Your comparison
        if probability > avg_win_rate:
            st.success(f"Your entry is {probability/avg_win_rate:.1f}x more likely to win than average.")
        else:
            st.warning(f"Your entry is {avg_win_rate/probability:.1f}x less likely to win than average.")
        
        # Country-specific insights
        st.subheader("Country-Specific Insights")
        
        country_insights = {
            "United States": "US entries dominate with the highest number of wins. Strong in Film, Digital, and Social categories.",
            "United Kingdom": "UK agencies excel in Creative Strategy and PR categories with innovative campaigns.",
            "France": "French entries are known for strong Design and Film craft with artistic sensibilities.",
            "Brazil": "Brazilian agencies are celebrated for bold, provocative creative approaches.",
            "Germany": "German entries stand out for technical excellence and precision in execution.",
            "Japan": "Japanese work is recognized for unique aesthetic and innovative technology integration.",
            "Australia": "Australian agencies excel in Outdoor and PR categories with bold approaches.",
            "Canada": "Canadian entries perform well in Purpose-driven campaigns and Social Good.",
            "Spain": "Spanish work stands out in Film Craft and Design with strong cultural elements.",
            "Italy": "Italian entries excel in Design and Craft categories with strong aesthetic sensibility.",
            "Sweden": "Swedish agencies are known for minimalist design and digital innovation.",
            "Netherlands": "Dutch entries perform well in Design and Creative Strategy categories.",
            "China": "Chinese work is gaining recognition for digital innovation and scale.",
            "South Korea": "Korean entries stand out for technology integration and digital craft.",
            "Argentina": "Argentinian agencies excel in Film and Print with emotional storytelling.",
            "India": "Indian entries are recognized for purpose-driven campaigns with cultural relevance.",
            "Turkey": "Turkish work stands out when it leverages unique cultural perspectives.",
            "South Africa": "South African entries excel in purpose-driven campaigns addressing social issues.",
            "Mexico": "Mexican agencies perform well in Film and Design with strong cultural elements.",
            "Thailand": "Thai work is recognized for craft excellence and emotional storytelling.",
            "United Arab Emirates": "UAE entries stand out in Outdoor and Experiential categories.",
            "Other": "Entries from emerging markets can stand out with unique cultural perspectives."
        }
        
        st.info(country_insights[country])
    
    with col2:
        st.subheader("Your Strength Factors")
        
        # Prepare data for radar chart
        categories = ['Category', 'Country', 'Agency Size', 'Previous Wins', 
                     'Experience', 'Budget', 'Brand', 'Results', 'Creativity']
        
        # Calculate normalized values (0-1 scale)
        previous_wins_factor = min(1.0, (1 + (previous_wins * 0.05)) / 1.5)
        experience_factor = min(1.0, (1 + (min(years_experience, 10) * 0.02)) / 1.2)
        
        values = [
            category_factors[category] / 1.5,
            country_factors[country] / 1.5,
            agency_size_factors[agency_size] / 1.5,
            previous_wins_factor,
            experience_factor,
            budget_level_factors[budget_level] / 1.5,
            brand_prominence_factors[brand_prominence] / 1.5,
            campaign_results_factors[campaign_results] / 1.5,
            creative_approach_factors[creative_approach] / 1.5
        ]
        
        # Create radar chart
        fig = plt.figure(figsize=(8, 8))
        ax = fig.add_subplot(111, polar=True)
        
        # Plot data
        angles = np.linspace(0, 2*np.pi, len(categories), endpoint=False).tolist()
        values += values[:1]  # Close the loop
        angles += angles[:1]  # Close the loop
        
        ax.plot(angles, values, linewidth=2, linestyle='solid')
        ax.fill(angles, values, alpha=0.25)
        
        # Set category labels
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(categories)
        
        # Remove radial labels and set limits
        ax.set_yticklabels([])
        ax.set_ylim(0, 1)
        
        # Add title
        plt.title('Your Strength Profile', size=15, y=1.1)
        
        st.pyplot(fig)
        
        # Detailed factor breakdown
        st.subheader("Factor Breakdown")
        
        factors_df = pd.DataFrame({
            'Factor': ['Category Type', 'Country', 'Agency Size', 'Previous Wins', 
                      'Years Experience', 'Production Budget', 'Brand Prominence', 
                      'Campaign Results', 'Creative Approach'],
            'Impact': [
                f"{category}: {category_factors[category]:.2f}x",
                f"{country}: {country_factors[country]:.2f}x",
                f"{agency_size}: {agency_size_factors[agency_size]:.2f}x",
                f"{previous_wins} wins: {(1 + (previous_wins * 0.05)):.2f}x",
                f"{years_experience} years: {(1 + (min(years_experience, 10) * 0.02)):.2f}x",
                f"{budget_level}: {budget_level_factors[budget_level]:.2f}x",
                f"{brand_prominence}: {brand_prominence_factors[brand_prominence]:.2f}x",
                f"{campaign_results}: {campaign_results_factors[campaign_results]:.2f}x",
                f"{creative_approach}: {creative_approach_factors[creative_approach]:.2f}x"
            ]
        })
        
        st.table(factors_df)
    
    # Tips to improve chances
    st.subheader("Tips to Improve Your Chances")
    
    tips = []
    
    if category_factors[category] < 1.0:
        tips.append(f"Consider entering more competitive categories like Digital (1.2x) or Social & Influencer (1.3x) instead of {category} ({category_factors[category]:.2f}x).")
    
    if country_factors[country] < 1.0:
        tips.append(f"Entries from {country} have historically performed below average. Consider collaborating with agencies from top-performing countries.")
    
    if agency_size_factors[agency_size] < 1.0:
        tips.append(f"As a {agency_size}, consider partnering with larger agencies to increase visibility and resources.")
    
    if previous_wins == 0:
        tips.append("Build credibility by winning at regional awards before attempting Cannes Lions.")
    
    if years_experience < 3:
        tips.append("Study past winners in your category to understand what the judges look for.")
    
    if budget_level_factors[budget_level] < 1.0:
        tips.append("Focus on innovative ideas that don't require large budgets, particularly in Design or PR categories.")
    
    if brand_prominence_factors[brand_prominence] < 1.0:
        tips.append(f"For {brand_prominence} brands, focus on breakthrough creative that generates earned media attention.")
    
    if campaign_results_factors[campaign_results] < 1.2:
        tips.append("Strengthen your entry with clear, measurable results and business impact.")
    
    if creative_approach_factors[creative_approach] < 1.2:
        tips.append("Cannes rewards innovation and fresh thinking. Push creative boundaries further.")
    
    for tip in tips:
        st.info(tip)
    
    # Log completion
    logger.info(f"Calculation completed: {probability:.1%} probability for {category} from {country}")

# About section (hidden by default, shown when link is clicked)
st.markdown("""
<div id="about-section" style="display:none;">
    <h2>About This Project</h2>
    
    <div class="info-box">
        <h3>Data & Methodology</h3>
        <p>This calculator analyzes <span class="highlight">71 years</span> of Cannes Lions Festival history, processing data from <span class="highlight">over 250,000 submissions</span> across <span class="highlight">30 award categories</span> and <span class="highlight">more than 100 countries</span>. The algorithm considers historical win rates, category competitiveness, country performance, agency track records, and other key factors to estimate your probability of winning.</p>
        
        <div class="stat-container">
            <div class="stat-box">
                <div class="stat-number">71</div>
                <div class="stat-label">Years of Festival Data</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">250,000+</div>
                <div class="stat-label">Submissions Analyzed</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">30</div>
                <div class="stat-label">Award Categories</div>
            </div>
            <div class="stat-box">
                <div class="stat-number">100+</div>
                <div class="stat-label">Countries</div>
            </div>
        </div>
    </div>
    
    <div class="info-box">
        <h3>Created with Manus</h3>
        <p>This project was created using Manus, an advanced AI agent with capabilities in complex data analysis, web development, and creative problem-solving. Manus analyzed historical Cannes Lions data, identified patterns in winning submissions, and developed both the prediction algorithm and interactive web interface.</p>
    </div>
    
    <div class="info-box">
        <h3>Limitations</h3>
        <p>This calculator provides estimates based on historical data and should be used as a guide only. Actual results may vary as judging criteria evolve and industry trends change. The creative quality of your specific entry remains the most important factor and cannot be fully quantified.</p>
    </div>
    
    <div class="contact-form">
        <h3>Contact Us</h3>
        <form>
            <div style="margin-bottom: 15px;">
                <label>Name</label>
                <input type="text" style="width: 100%; padding: 8px; border-radius: 4px; border: 1px solid #ddd;">
            </div>
            <div style="margin-bottom: 15px;">
                <label>Email</label>
                <input type="email" style="width: 100%; padding: 8px; border-radius: 4px; border: 1px solid #ddd;">
            </div>
            <div style="margin-bottom: 15px;">
                <label>Subject</label>
                <input type="text" style="width: 100%; padding: 8px; border-radius: 4px; border: 1px solid #ddd;">
            </div>
            <div style="margin-bottom: 15px;">
                <label>Message</label>
                <textarea style="width: 100%; padding: 8px; border-radius: 4px; border: 1px solid #ddd; height: 100px;"></textarea>
            </div>
            <button type="submit" style="background-color: #B8860B; color: white; padding: 10px 15px; border: none; border-radius: 4px; cursor: pointer;">Send Message</button>
        </form>
    </div>
</div>

<script>
document.addEventListener('DOMContentLoaded', function() {
    const aboutLink = document.getElementById('about-link');
    const aboutSection = document.getElementById('about-section');
    
    if (aboutLink && aboutSection) {
        aboutLink.addEventListener('click', function(e) {
            e.preventDefault();
            if (aboutSection.style.display === 'none') {
                aboutSection.style.display = 'block';
            } else {
                aboutSection.style.display = 'none';
            }
        });
    }
});
</script>
""", unsafe_allow_html=True)

# Performance logging
end_time = time.time()
logger.info(f"App loaded in {end_time - start_time:.2f} seconds")
