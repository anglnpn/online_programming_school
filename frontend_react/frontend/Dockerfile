
FROM node:21

WORKDIR ./frontend_react/frontend

COPY package*.json ./

RUN npm install

COPY . .

CMD ["npm", "start"]
