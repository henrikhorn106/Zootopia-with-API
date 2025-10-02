# Zootopia with API 🦁🐼🦒

A Python-based web application that dynamically generates animal information pages by fetching data from external APIs. This project creates an interactive zoo directory with detailed information about various animals.

## 📋 Project Description

Zootopia with API is a tool designed to automatically generate beautiful, informative web pages about animals. The application retrieves animal data from external APIs and formats it into an HTML page, making it easy to create and maintain a digital zoo catalog.

**Key Features:**
- Fetches real-time animal data from APIs
- Generates static HTML pages with animal information
- Displays animal characteristics, habitat, diet, and conservation status
- Clean, responsive web interface
- Easy to extend with additional animals

**Target Audience:**
- Educators creating educational resources about animals
- Wildlife enthusiasts building animal databases
- Students learning about API integration and web development
- Zoo organizations needing digital animal catalogs

## 🛠️ Technologies Used

- **Python 3.x** - Core programming language
- **Requests** - HTTP library for API calls
- **HTML/CSS** - Frontend presentation
- **External Animal APIs** - Data source for animal information

## 📦 Installation

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/henrikhorn106/Zootopia-with-API.git
   cd Zootopia-with-API
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   
   Or install manually:
   ```bash
   pip install requests
   ```

3. **Configure API credentials (if required):**
   - Check if the API requires an API key
   - Create a `config.py` file or set environment variables
   - Add your API credentials

## 🚀 Usage

### Basic Usage

Run the main script to generate the animal web page:

```bash
python animals_web_generator.py
```

This will:
1. Fetch animal data from the configured API
2. Process and format the data
3. Generate an HTML file with the animal information
4. Save the output (typically as `animals.html`)

### Viewing the Results

Open the generated HTML file in your web browser:

```bash
# On macOS
open animals.html

# On Linux
xdg-open animals.html

# On Windows
start animals.html
```

### Customization

You can customize the animals displayed by modifying the animal list in the script:

```python
animals = ["Lion", "Elephant", "Giraffe", "Panda"]
```

### Example Output

The generated page will include:
- Animal name and scientific classification
- Physical characteristics (size, weight, lifespan)
- Habitat and geographic distribution
- Diet and feeding behavior
- Conservation status
- Fun facts

## 📁 Project Structure

```
Zootopia-with-API/
│
├── animals_web_generator.py   # Main script for generating web pages
├── requirements.txt            # Python dependencies
├── templates/                  # HTML templates (if applicable)
├── static/                     # CSS and static assets (if applicable)
├── animals.html               # Generated output file
└── README.md                  # This file
```

## 🔧 Configuration

### API Selection

The project can work with various animal APIs. Common options include:

- **API Ninjas Animals API** - Comprehensive animal data
- **Zoo Animal API** - Detailed zoo animal information
- **Custom API** - Use your own data source

Update the API endpoint in the script:

```python
API_URL = "https://api.example.com/animals"
```

## 🤝 Contributing

Contributions are welcome! Here's how you can help improve Zootopia with API:

### How to Contribute

1. **Fork the repository**
   - Click the "Fork" button at the top right of this page

2. **Clone your fork**
   ```bash
   git clone https://github.com/your-username/Zootopia-with-API.git
   cd Zootopia-with-API
   ```

3. **Create a feature branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Make your changes**
   - Write clean, commented code
   - Follow Python PEP 8 style guidelines
   - Test your changes thoroughly

5. **Commit your changes**
   ```bash
   git add .
   git commit -m "Add: description of your changes"
   ```

6. **Push to your fork**
   ```bash
   git push origin feature/your-feature-name
   ```

7. **Create a Pull Request**
   - Go to the original repository
   - Click "New Pull Request"
   - Select your feature branch
   - Describe your changes clearly

### Contribution Ideas

- Add support for additional APIs
- Improve the HTML/CSS styling
- Add error handling and validation
- Create unit tests
- Add support for images
- Implement caching for API responses
- Add search and filter functionality
- Create documentation for new features

### Code Style

- Follow PEP 8 conventions
- Write descriptive variable and function names
- Add docstrings to functions and classes
- Keep functions focused and modular

## 📝 License

This project is open source. Please check the repository for license information.

## 🐛 Troubleshooting

### Common Issues

**API Connection Errors:**
- Check your internet connection
- Verify API endpoint is correct
- Ensure API key is valid (if required)

**Missing Dependencies:**
```bash
pip install --upgrade -r requirements.txt
```

**Permission Errors:**
- Ensure you have write permissions in the project directory
- Run with appropriate permissions if needed

## 📞 Contact

For questions, suggestions, or issues:
- Open an issue on GitHub
- Contact the repository owner: [@henrikhorn106](https://github.com/henrikhorn106)

## 🙏 Acknowledgments

- Animal data provided by external APIs
- Inspired by the need for accessible wildlife information
- Built as a learning project for API integration

---

**Made with 🦁 by Henrik Horn**