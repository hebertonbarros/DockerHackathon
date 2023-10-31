# Use the official Node.js image as the base image
FROM node:14

# Set the working directory in the container
WORKDIR /app

# Copy the package.json and package-lock.json files to the container
COPY ./package*.json ./

# Install the project dependencies
RUN npm install

# Copy the entire frontend code to the container
COPY . .

# Build the React application
# RUN npm run build

# Expose port 3000 for the React application
EXPOSE 3000

# Start the React application
CMD ["npm", "start"]
# ENTRYPOINT ["tail"]

