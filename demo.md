在 `highlight.js` 11.11.1 版本中，`highlightBlock` 方法已经被废弃，官方推荐使用新的 `highlightElement` 方法或者直接调用 `highlight` 方法。以下是如何自定义高亮代码，并获取代码块的语言的示例。

---

### 方案：使用 `highlight.js` 的新 API `highlight` 或 `highlightElement`

#### 方法一：通过 `highlight` 手动高亮代码（推荐）

`highlight` 方法允许我们直接指定语言，并返回高亮后的 HTML。

```typescript
import hljs from "highlight.js";
import "highlight.js/styles/atom-one-dark.css";

export default function (el: HTMLElement) {
  // 获取所有 <pre> 标签
  const blocks = el.querySelectorAll("pre code");

  blocks.forEach((block: HTMLElement) => {
    const code = block.innerText; // 获取代码内容
    const lang = block.className.replace("language-", ""); // 获取语言名称

    if (lang && hljs.getLanguage(lang)) {
      // 如果指定了语言，使用该语言高亮
      const result = hljs.highlight(code, { language: lang });
      block.innerHTML = result.value;
    } else {
      // 如果没有指定语言，自动检测
      const result = hljs.highlightAuto(code);
      block.innerHTML = result.value;

      // 自动检测语言后，可以通过 result.language 拿到检测到的语言
      block.setAttribute(
        "data-detected-language",
        result.language || "unknown"
      );
    }

    // 添加 hljs 类名以应用样式
    block.classList.add("hljs");
  });
}
```

---

#### 方法二：使用 `highlightElement` 自动高亮（适合动态渲染内容）

`highlightElement` 方法会根据 `<code>` 元素的 `class` 自动检测语言。

```typescript
import hljs from "highlight.js";
import "highlight.js/styles/atom-one-dark.css";

export default function (el: HTMLElement) {
  // 获取所有 <pre><code> 标签
  const blocks = el.querySelectorAll("pre code");

  blocks.forEach((block: HTMLElement) => {
    // 自动检测并高亮代码
    hljs.highlightElement(block);

    // 获取语言
    const detectedLang = block.getAttribute("class")?.replace("language-", "");
    console.log("Detected language:", detectedLang || "unknown");
  });
}
```

---

### 区别

| 方法               | 使用场景                        | 优点                                                                       | 缺点                            |
| ------------------ | ------------------------------- | -------------------------------------------------------------------------- | ------------------------------- |
| `highlight`        | 手动传入代码和语言              | 灵活，可以完全控制代码高亮的逻辑。支持自动检测语言并获取检测结果。         | 需要自己管理代码内容和语言。    |
| `highlightElement` | 自动从 DOM 获取代码和语言并高亮 | 简单，直接操作 DOM 元素，支持从 `class` 属性中获取语言信息，无需额外处理。 | 只能用于静态渲染后的 DOM 内容。 |

---

### 获取语言并添加自定义逻辑

以下示例展示如何获取语言，并在语言匹配后添加自定义逻辑：

```typescript
import hljs from "highlight.js";
import "highlight.js/styles/atom-one-dark.css";

export default function (el: HTMLElement) {
  // 获取所有 <pre><code> 标签
  const blocks = el.querySelectorAll("pre code");

  blocks.forEach((block: HTMLElement) => {
    // 自动检测并高亮代码
    hljs.highlightElement(block);

    // 获取语言
    const lang = block.className.replace("language-", "");
    if (lang === "javascript") {
      console.log("This is JavaScript code!");
    } else if (lang === "python") {
      console.log("This is Python code!");
    } else {
      console.log("Unknown or no language detected.");
    }
  });
}
```

---

### 自定义扩展高亮逻辑

如果需要完全自定义逻辑，可以手动构造高亮的结果：

```typescript
import hljs from "highlight.js";
import "highlight.js/styles/atom-one-dark.css";

export default function (el: HTMLElement) {
  // 获取所有 <pre><code> 标签
  const blocks = el.querySelectorAll("pre code");

  blocks.forEach((block: HTMLElement) => {
    const code = block.innerText; // 获取代码内容
    const lang = block.className.replace("language-", ""); // 获取语言

    let highlightedCode = "";

    if (lang && hljs.getLanguage(lang)) {
      // 使用指定语言高亮
      highlightedCode = hljs.highlight(code, { language: lang }).value;
    } else {
      // 自动检测语言并高亮
      const result = hljs.highlightAuto(code);
      highlightedCode = result.value;

      // 如果需要，可以在这里获取检测到的语言
      console.log("Detected language:", result.language || "unknown");
    }

    // 自定义处理高亮后的 HTML
    block.innerHTML = highlightedCode;
    block.classList.add("hljs");
  });
}
```

---

### 动态渲染时如何高亮

如果代码块是通过异步渲染（如 `v-for` 或 `v-if`）动态生成的，可以在数据加载完成后调用高亮方法：

#### 在 Vue 组件中：

```vue
<template>
  <div ref="codeContainer">
    <pre><code class="language-javascript">console.log('Hello, World!');</code></pre>
    <pre><code class="language-python">print('Hello, World!')</code></pre>
  </div>
</template>

<script lang="ts">
import { onMounted, ref } from "vue";
import hljs from "highlight.js";
import "highlight.js/styles/atom-one-dark.css";

export default {
  name: "CodeHighlighter",
  setup() {
    const codeContainer = ref<HTMLElement | null>(null);

    onMounted(() => {
      if (codeContainer.value) {
        const blocks = codeContainer.value.querySelectorAll("pre code");
        blocks.forEach((block) => {
          hljs.highlightElement(block as HTMLElement);
        });
      }
    });

    return { codeContainer };
  },
};
</script>
```

---

### 总结

- `highlight.js` 11+ 推荐使用 `highlight` 和 `highlightElement` 方法。
- 如果需要获取语言，可以通过 `class` 属性或 `highlightAuto` 的返回值。
- 适配动态渲染时，记得在 DOM 完成更新后调用高亮逻辑。

这两种方式都可以很好地适配你的场景。选择具体方法时，可以根据项目需求决定。
