在 CSS 中，通过 `cursor` 属性可以设置鼠标在不同状态下的形状。要实现“鼠标抓东西”的效果，你可以使用 CSS 的 `cursor` 属性和一些特定的值，如 `grab` 和 `grabbing`。

### 示例代码

```css
.grabbable {
    cursor: grab; /* 默认抓取效果 */
}

.grabbable:active {
    cursor: grabbing; /* 当点击/按住时显示抓取中的效果 */
}
```

### 效果说明

1. **`grab`**:
   - 鼠标显示为一个手的形状，表示可以拖动或抓取的元素。
2. **`grabbing`**:
   - 鼠标显示为一个抓紧的手的形状，表示正在抓取或拖动元素。

------

### 示例 HTML 和完整代码

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>抓东西效果</title>
    <style>
        .grabbable {
            cursor: grab;
            width: 200px;
            height: 100px;
            background-color: lightblue;
            border: 2px solid #333;
            display: flex;
            align-items: center;
            justify-content: center;
            user-select: none; /* 禁止选中文字 */
        }

        .grabbable:active {
            cursor: grabbing;
            background-color: lightcoral; /* 抓取时改变背景颜色（可选） */
        }
    </style>
</head>
<body>
    <div class="grabbable">抓我试试</div>
</body>
</html>
```

------

### 实现可拖动功能（可选）

如果你想让元素不仅有抓取效果，还能通过鼠标拖动移动，可以结合 JavaScript 来实现。

#### 可拖动示例

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>抓东西拖动</title>
    <style>
        .draggable {
            cursor: grab;
            width: 200px;
            height: 100px;
            background-color: lightblue;
            border: 2px solid #333;
            position: absolute;
            top: 100px;
            left: 100px;
            display: flex;
            align-items: center;
            justify-content: center;
            user-select: none;
        }

        .draggable:active {
            cursor: grabbing;
        }
    </style>
</head>
<body>
    <div class="draggable">拖动我</div>

    <script>
        const draggable = document.querySelector('.draggable');

        let isDragging = false;
        let offsetX = 0, offsetY = 0;

        draggable.addEventListener('mousedown', (e) => {
            isDragging = true;
            offsetX = e.offsetX;
            offsetY = e.offsetY;
            draggable.style.cursor = 'grabbing';
        });

        document.addEventListener('mousemove', (e) => {
            if (!isDragging) return;
            draggable.style.left = `${e.pageX - offsetX}px`;
            draggable.style.top = `${e.pageY - offsetY}px`;
        });

        document.addEventListener('mouseup', () => {
            isDragging = false;
            draggable.style.cursor = 'grab';
        });
    </script>
</body>
</html>
```

### 说明

1. **HTML**:
   - 创建一个可拖动的元素。
2. **CSS**:
   - 使用 `cursor: grab` 和 `cursor: grabbing` 设置鼠标形状。
   - 使用 `position: absolute` 让元素可以通过 JavaScript 改变位置。
3. **JavaScript**:
   - `mousedown`: 记录鼠标按下的位置并开启拖动模式。
   - `mousemove`: 实时更新元素的位置。
   - `mouseup`: 停止拖动模式。

完成后，你可以拖动元素，同时鼠标形状会动态改变，非常直观！