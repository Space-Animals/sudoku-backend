curl "http://localhost:8000/games/${ID}/" \
  --include \
  --request DELETE \
  --header "X-CSRFToken: ${CSRF}" \
  --header "Authorization: Token ${TOKEN}" \

echo
