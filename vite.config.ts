import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import svgLoader from 'vite-svg-loader'
import path from 'path'

const svgLoaderConfig = {
  svgoConfig: {
    plugins: [
      {
        name: "preset-default",
        params: {
          overrides: {
            removeViewBox: false, // 保留 viewBox 属性，确保 SVG 可以自适应大小
          },
        },
      },
    ],
  },
}

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue(), svgLoader(svgLoaderConfig as any),],
  resolve: {
    alias: {
      '@': path.resolve(__dirname, 'src')
    }
  },
  server: {
    proxy: {
      '/auth': {
        target: 'http://112.74.75.211:8000/api',
        changeOrigin: true,
        // rewrite: (path) => path.replace(/^\/api/, '')
      }
    }
  }
})
