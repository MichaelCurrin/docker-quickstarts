FROM node:14

WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install --production --loglevel warn && \
  npm cache clean --force

COPY . .

CMD ["npm", "start"]
