import re

with open('produk.html', 'r') as f:
    html_content = f.read()

start_marker = "  <!-- Page Hero -->"
end_marker = "  <!-- CTA Section -->"

start_idx = html_content.find(start_marker)
end_idx = html_content.find(end_marker)

new_html = """  <!-- Produk Table Section -->
  <section class="produk-table-section">
    <div class="container">
      <div class="pts-header">
        <h1>Produk</h1>
        <p>Dapatkan produk terkini dari rakan ponsel digital dan cek detail produk yang anda inginkan</p>
      </div>

      <div class="pts-table-card">
        <div class="pts-controls">
          <div class="pts-show">
            Show <select><option>10</option></select> entries
          </div>
          <div class="pts-filters">
            <div class="pts-search">
              <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
              <input type="text" placeholder="Search...">
            </div>
            <div class="pts-sort">
              Short by : <select><option>Newest</option></select>
            </div>
            <div class="pts-sort">
              Short by : <select><option>Kategori</option></select>
            </div>
          </div>
        </div>

        <div class="pts-table-wrapper">
          <table class="pts-table">
            <thead>
              <tr>
                <th>No <span class="sort-icon"></span></th>
                <th>Kode <span class="sort-icon"></span></th>
                <th>Kategori <span class="sort-icon"></span></th>
                <th>Nama Produk <span class="sort-icon"></span></th>
                <th class="text-right">Status <span class="sort-icon"></span></th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>1</td>
                <td>S5</td>
                <td>Pulsa Reguler</td>
                <td>Pulsa Reguler Telkomsel 5.000</td>
                <td class="text-right"><span class="badge badge-success"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg> Tersedia</span></td>
              </tr>
              <tr>
                <td>2</td>
                <td>S10</td>
                <td>Pulsa Reguler</td>
                <td>Pulsa Reguler Telkomsel 10.000</td>
                <td class="text-right"><span class="badge badge-warning"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><polyline points="19 12 12 19 5 12"/></svg> Harga Turun</span></td>
              </tr>
              <tr>
                <td>3</td>
                <td>PL20</td>
                <td>Token</td>
                <td>Token Listrik Standart 20.000</td>
                <td class="text-right"><span class="badge badge-primary"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="19" x2="12" y2="5"/><polyline points="5 12 12 5 19 12"/></svg> Harga Naik</span></td>
              </tr>
              <tr>
                <td>4</td>
                <td>STP25</td>
                <td>Pulsa Transfer</td>
                <td>Pulsa Transfer Telkomsel 25.000</td>
                <td class="text-right"><span class="badge badge-success"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg> Tersedia</span></td>
              </tr>
              <tr>
                <td>5</td>
                <td>T25</td>
                <td>Pulsa Reguler</td>
                <td>Pulsa Reguler Three 25.000</td>
                <td class="text-right"><span class="badge badge-success"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg> Tersedia</span></td>
              </tr>
              <tr>
                <td>6</td>
                <td>IN45</td>
                <td>Pulsa Reguler</td>
                <td>Pulsa Reguler Indosat 45.000</td>
                <td class="text-right"><span class="badge badge-warning"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="5" x2="12" y2="19"/><polyline points="19 12 12 19 5 12"/></svg> Harga Turun</span></td>
              </tr>
              <tr>
                <td>7</td>
                <td>SM50</td>
                <td>Pulsa Reguler</td>
                <td>Pulsa Reguler Smartfren 50.000</td>
                <td class="text-right"><span class="badge badge-success"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg> Tersedia</span></td>
              </tr>
              <tr>
                <td>8</td>
                <td>SM70</td>
                <td>Pulsa Reguler</td>
                <td>Pulsa Reguler Smartfren 70.000</td>
                <td class="text-right"><span class="badge badge-success"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="20 6 9 17 4 12"/></svg> Tersedia</span></td>
              </tr>
              <tr>
                <td>9</td>
                <td>LA90</td>
                <td>e-Wallet</td>
                <td>Saldo LinkAja 90.000</td>
                <td class="text-right"><span class="badge badge-danger"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><line x1="4.93" y1="4.93" x2="19.07" y2="19.07"/></svg> Gangguan</span></td>
              </tr>
              <tr>
                <td>10</td>
                <td>LA100</td>
                <td>e-Wallet</td>
                <td>Saldo LinkAja 100.000</td>
                <td class="text-right"><span class="badge badge-primary"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="19" x2="12" y2="5"/><polyline points="5 12 12 5 19 12"/></svg> Harga Naik</span></td>
              </tr>
            </tbody>
          </table>
        </div>

        <div class="pts-footer">
          <div class="pts-info">Showing data 1 to 10 of 256K entries</div>
          <div class="pts-pagination">
            <button>&lt;</button>
            <button class="active">1</button>
            <button>2</button>
            <button>3</button>
            <button>4</button>
            <span class="dots">...</span>
            <button>40</button>
            <button>&gt;</button>
          </div>
        </div>
      </div>
    </div>
  </section>
"""

new_content = html_content[:start_idx] + new_html + html_content[end_idx:]

with open('produk.html', 'w') as f:
    f.write(new_content)

css = """
/* ===== PRODUK TABLE SECTION ===== */
.produk-table-section {
  padding: 100px 0 80px;
  background: linear-gradient(180deg, #FAFAFA 0%, #FFFFFF 100%);
  min-height: 100vh;
}

.pts-header {
  text-align: center;
  margin-bottom: 40px;
}

.pts-header h1 {
  font-size: 2.2rem;
  font-weight: 800;
  color: var(--secondary);
  margin-bottom: 12px;
}

.pts-header p {
  font-size: 1rem;
  color: var(--text-gray);
  max-width: 600px;
  margin: 0 auto;
}

.pts-table-card {
  background: var(--white);
  border-radius: var(--radius-xl);
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.04);
  padding: 32px;
}

.pts-controls {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 24px;
  flex-wrap: wrap;
  gap: 16px;
}

.pts-show {
  font-size: 0.85rem;
  color: var(--text-gray);
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 8px;
}

.pts-show select {
  padding: 6px 12px;
  border: 1px solid var(--border);
  border-radius: 6px;
  background: #F8FAFC;
  outline: none;
  font-family: inherit;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
}

.pts-filters {
  display: flex;
  gap: 16px;
  align-items: center;
}

.pts-search {
  position: relative;
}

.pts-search svg {
  position: absolute;
  left: 12px;
  top: 50%;
  transform: translateY(-50%);
  width: 16px;
  height: 16px;
  color: var(--text-light);
}

.pts-search input {
  padding: 10px 16px 10px 36px;
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  font-size: 0.85rem;
  width: 240px;
  outline: none;
  font-family: inherit;
  transition: border-color 0.2s;
}

.pts-search input:focus {
  border-color: var(--primary);
}

.pts-sort {
  font-size: 0.85rem;
  color: var(--text-gray);
  display: flex;
  align-items: center;
  gap: 8px;
}

.pts-sort select {
  padding: 10px 16px;
  border: 1px solid var(--border);
  border-radius: var(--radius-sm);
  font-family: inherit;
  font-size: 0.85rem;
  font-weight: 600;
  color: var(--text-dark);
  outline: none;
  cursor: pointer;
  background: var(--white);
}

.pts-table-wrapper {
  overflow-x: auto;
  margin-bottom: 24px;
}

.pts-table {
  width: 100%;
  border-collapse: collapse;
  min-width: 800px;
}

.pts-table th,
.pts-table td {
  padding: 16px 20px;
  text-align: left;
  border-bottom: 1px solid var(--border);
  font-size: 0.9rem;
}

.pts-table th {
  color: var(--text-dark);
  font-weight: 700;
  position: relative;
  cursor: pointer;
}

.pts-table td {
  color: var(--text-dark);
  font-weight: 500;
}

.sort-icon {
  display: inline-block;
  width: 0;
  height: 0;
  border-left: 4px solid transparent;
  border-right: 4px solid transparent;
  border-bottom: 5px solid var(--text-light);
  margin-left: 6px;
  vertical-align: middle;
}

.pts-table th:hover .sort-icon {
  border-bottom-color: var(--primary);
}

.text-right {
  text-align: right !important;
}

.badge {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  padding: 6px 16px;
  border-radius: 100px;
  font-size: 0.8rem;
  font-weight: 700;
}

.badge svg {
  width: 14px;
  height: 14px;
}

.badge-success {
  background: #ECFDF5;
  color: #10B981;
}

.badge-warning {
  background: #FFFBEB;
  color: #F59E0B;
}

.badge-primary {
  background: #EFF6FF;
  color: #3B82F6;
}

.badge-danger {
  background: #FEF2F2;
  color: #EF4444;
}

.pts-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  flex-wrap: wrap;
  gap: 16px;
}

.pts-info {
  font-size: 0.85rem;
  color: var(--text-light);
  font-weight: 500;
}

.pts-pagination {
  display: flex;
  gap: 6px;
  align-items: center;
}

.pts-pagination button {
  width: 36px;
  height: 36px;
  border-radius: 6px;
  border: none;
  background: #F8FAFC;
  color: var(--text-dark);
  font-family: inherit;
  font-size: 0.85rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.pts-pagination button:hover {
  background: #E2E8F0;
}

.pts-pagination button.active {
  background: var(--primary);
  color: var(--white);
}

.pts-pagination .dots {
  color: var(--text-light);
  font-weight: 600;
  padding: 0 4px;
}

@media (max-width: 1024px) {
  .pts-controls {
    flex-direction: column;
    align-items: flex-start;
  }
  
  .pts-filters {
    flex-wrap: wrap;
    width: 100%;
  }
  
  .pts-search input {
    width: 100%;
  }
}
"""

with open('style.css', 'r') as f:
    style_content = f.read()

if '/* ===== PRODUK TABLE SECTION ===== */' not in style_content:
    with open('style.css', 'w') as f:
        f.write(style_content + "\n" + css)
