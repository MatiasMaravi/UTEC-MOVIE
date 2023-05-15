build:
	npm run build
deploy:build
	aws s3 cp --recursive dist/ s3://frontend-vue3 --grants read=uri=http://acs.amazonaws.com/groups/global/AllUsers