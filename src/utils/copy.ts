export function copy(text: string): Promise<boolean> {
  if (navigator.clipboard && navigator.clipboard.writeText) {
    // 使用 navigator.clipboard 复制
    return navigator.clipboard
      .writeText(text)
      .then(() => {
        return true; // 成功时返回 true
      })
      .catch((err) => {
        console.error("复制失败:", err);
        return false; // 失败时返回 false
      });
  } else {
    // 使用 document.execCommand 作为回退方案
    return new Promise((resolve, reject) => {
      const textarea = document.createElement("textarea");
      textarea.value = text;
      textarea.style.position = "fixed"; // 避免页面滚动
      textarea.style.opacity = "0"; // 隐藏 textarea
      document.body.appendChild(textarea);
      textarea.focus();
      textarea.select();
      try {
        const success = document.execCommand("copy");
        resolve(success); // 返回成功或失败的结果
      } catch (err) {
        console.error("复制失败:", err);
        reject(false); // 返回失败
      } finally {
        document.body.removeChild(textarea); // 移除临时 textarea
      }
    });
  }
}
