import os
import re

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for file in html_files:
    with open(file, 'r') as f:
        content = f.read()

    # The problem is there is an extra `</div>` immediately following the new `.rakanpay-logo` blocks in the footer because of the non-greedy match issue.
    # Let's see the exact text:
    #         </div>
    #         </div>
    #         <div class="fn-social">
    # Wait, let's fix it safely by removing the specific extra </div> that closes `.fn-brand` prematurely.
    
    # Actually, a better way is to find `<div class="fn-brand">` and everything inside it, and re-construct it properly.
    # Let's fix the specific string match where the extra `</div>` is placed before `<div class="fn-social">`.
    content = content.replace("        </div>\n        </div>\n        <div class=\"fn-social\">", "        </div>\n        <div class=\"fn-social\">")
    
    # Also need to check if the same happened to `.footer-logo` in the old footer.
    # Old footer had `<div class="footer-logo">...</div>`. If it had an inner `<div>`, it might also have an extra `</div>`.
    # Let's just fix the double `</div></div>` for `.footer-logo` as well.
    content = content.replace("        </div>\n        </div>\n        <p class=\"footer-desc\">", "        </div>\n        <p class=\"footer-desc\">")
    content = content.replace("</div>\n        </div>\n        <p class=\"footer-desc\">", "</div>\n        <p class=\"footer-desc\">")

    with open(file, 'w') as f:
        f.write(content)
