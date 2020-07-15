curl "http://localhost:8000/games/" \
  --include \
  --request GET \
  --header "Authorization: Token ${TOKEN}" \

echo
