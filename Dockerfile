FROM node:16 as base-builder

WORKDIR /app

FROM base-builder as build_be

COPY ./backend/package.json ./backend/package-lock.json*  /app/backend/
RUN cd ./backend && npm i --save
ADD ./backend ./backend
RUN cd ./backend && npm run build

FROM base-builder as build_fe

COPY ./frontend/package.json ./frontend/package-lock.json* /app/frontend/
RUN cd ./frontend && npm i --save
ADD ./frontend ./frontend
RUN cd ./frontend && npm run generate



FROM node:16-alpine

WORKDIR /app
COPY --from=build_be /app/backend /app
COPY --from=build_fe /app/frontend/dist /app/static

CMD cd /app && npm run start
