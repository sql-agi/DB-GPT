FROM node:20-alpine3.19 as builder

WORKDIR /app
COPY . .
# 安装
RUN npm i 
# 构建
RUN npm run build


FROM nginx:1.27.0-alpine

COPY --from=builder /app/dist /usr/share/nginx/html


