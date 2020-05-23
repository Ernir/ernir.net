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
