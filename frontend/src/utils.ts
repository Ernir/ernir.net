function escape(s: string): string {
  return s.replace(/([.*+?^${}()|[\]/\\])/g, "\\$1");
}

// Source: https://stackoverflow.com/a/25346429/1675015
function getCookie(name: string): string | null {
  const match = document.cookie.match(
    RegExp("(?:^|;\\s*)" + escape(name) + "=([^;]*)")
  );
  return match ? match[1] : null;
}

function getCsrfToken(): string | null {
  return getCookie("csrftoken");
}

export default getCsrfToken;

/*
 * From https://stackoverflow.com/a/6274381/1675015
 */
export function shuffle(a: any[]) {
  for (let i = a.length - 1; i > 0; i--) {
    const j = Math.floor(Math.random() * (i + 1));
    [a[i], a[j]] = [a[j], a[i]];
  }
  return a;
}
