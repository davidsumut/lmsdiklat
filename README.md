# LMS Diklat

## Overview
LMS Diklat is a Learning Management System designed to facilitate educational and training programs. It provides features for course management, user enrollment, and progress tracking.

## Setup Instructions

### Prerequisites
Before you begin, ensure you have the following installed:
- [Node.js](https://nodejs.org/) (version 14 or above)
- [npm](https://www.npmjs.com/) (Node package manager)
- [MongoDB](https://www.mongodb.com/) (for database management)

### Installation Steps
1. **Clone the Repository**  
   Open your terminal and run the following command:
   ```bash
   git clone https://github.com/davidsumut/lmsdiklat.git
   cd lmsdiklat
   ```

2. **Install Dependencies**  
   Run the following command to install all required packages:
   ```bash
   npm install
   ```

3. **Configure Environment Variables**  
   Create a `.env` file in the root directory and add your configuration:
   ```plaintext
   MONGODB_URI=your_mongodb_uri
   PORT=3000
   ```
   Replace `your_mongodb_uri` with your actual MongoDB connection string.

4. **Run the Application**  
   You can start the application using:
   ```bash
   npm start
   ```
   The application should now be running on `http://localhost:3000`. 

5. **Access the Application**  
   Open your web browser and visit `http://localhost:3000` to access the LMS Diklat application.

### Additional Information
- For more details on how to use the system, please refer to the [Wiki](https://github.com/davidsumut/lmsdiklat/wiki).
- Consider looking at the [Issues](https://github.com/davidsumut/lmsdiklat/issues) section for known bugs and feature requests.

## Contributing
If you would like to contribute to LMS Diklat, please fork the repository and create a pull request detailing your changes.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.