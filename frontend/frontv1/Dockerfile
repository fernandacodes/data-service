# Use the official Node.js image based on Node.js v22.1.0
FROM node:22.1.0

# Install http-server globally (assuming you want to serve the built Vue app)
RUN npm install -g http-server

# Set the working directory inside the container
WORKDIR /code

# Copy necessary configuration and source files
COPY frontend/frontv1/tsconfig.app.json ./tsconfig.app.json
COPY frontend/frontv1/src ./src
COPY frontend/frontv1/vite.config.ts ./vite.config.ts
COPY frontend/frontv1/tsconfig.node.json ./tsconfig.node.json
COPY frontend/frontv1/package.json ./package.json
COPY frontend/frontv1/index.html ./index.html
COPY frontend/frontv1/package-lock.json ./package-lock.json
COPY frontend/frontv1/tailwind.config.js ./tailwind.config.js
COPY frontend/frontv1/postcss.config.js ./postcss.config.js
COPY frontend/frontv1/tsconfig.json ./tsconfig.json

# Install dependencies
RUN npm install

# Build the Vue application
RUN npm run build

# Expose the port that http-server will run on (default is 8080)
EXPOSE 8080

# Command to serve the built Vue application using http-server
CMD [ "http-server", "dist" ]
