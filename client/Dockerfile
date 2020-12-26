FROM node:alpine
WORKDIR /app
COPY package.json .
COPY package-lock.json .
RUN npm ci
COPY . .
CMD npm start -- --disable-host-check --host 0.0.0.0