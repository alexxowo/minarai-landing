# Stage 1: Build
FROM node:22-alpine AS build

WORKDIR /app

COPY package.json package-lock.json ./
RUN npm ci

COPY . .
RUN npm run build

# Stage 2: Serve
FROM nginx:alpine AS runtime

# Default port (can be overridden at runtime with -e PORT=XXXX)
ENV PORT=8002

COPY nginx.conf /etc/nginx/nginx.conf.template
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE ${PORT}

# Substitute $PORT in the nginx config, then start nginx
CMD ["/bin/sh", "-c", "envsubst '${PORT}' < /etc/nginx/nginx.conf.template > /etc/nginx/nginx.conf && nginx -g 'daemon off;'"]
