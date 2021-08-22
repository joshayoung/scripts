#!/bin/bash

# Modified from:
# https://mhagemann.medium.com/how-to-change-the-user-for-all-your-git-commits-ffefbacf2652

echo "Provide a value for 'OLD_EMAIL' and 'NEW_EMAIL' below."
echo "Then comment-out the 'exit 1' below."
exit 1

git filter-branch --env-filter '
OLD_EMAIL=""
NEW_EMAIL=""
if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
then
  export GIT_COMMITTER_EMAIL="$NEW_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
then
  export GIT_AUTHOR_EMAIL="$NEW_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags

echo "Follow this script up with these two commands:"
echo "git push origin --force --all"
echo "git push origin --force --tags"
