css = """
/* ===== PARTNER LOGOS ===== */
.partners {
  padding: 40px 0;
  background: var(--white);
  border-top: 1px solid var(--border-color);
  border-bottom: 1px solid var(--border-color);
  overflow: hidden;
}

.partners-inner {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 60px;
  flex-wrap: wrap;
  opacity: 0.6;
}

.partner-logo {
  display: flex;
  align-items: center;
  gap: 8px;
  font-weight: 700;
  font-size: 1.25rem;
  color: var(--text-gray);
  letter-spacing: -0.02em;
}

.partner-logo svg {
  width: 28px;
  height: 28px;
}
"""

with open('style.css', 'r') as f:
    content = f.read()

# Insert the partners CSS right before .stats
content = content.replace(".stats {\n  padding: 80px 0;", css + "\n.stats {\n  padding: 80px 0;")

with open('style.css', 'w') as f:
    f.write(content)

