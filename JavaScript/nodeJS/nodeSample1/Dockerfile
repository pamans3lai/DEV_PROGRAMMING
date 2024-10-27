FROM node:23-alpine

RUN mkdir -p /home/ai/DEV_PROGRAMMING/JavaScript/nodeJS/nodeSample1/app/node_modules && chown -R node:node /home/ai/DEV_PROGRAMMING/JavaScript/nodeJS/nodeSample1/app

WORKDIR /home/ai/DEV_PROGRAMMING/JavaScript/nodeJS/nodeSample1/app

COPY package*.json ./ 

USER node

RUN npm install

COPY --chown=node:node . .

EXPOSE 3000

CMD [ "node", "server.js" ]
