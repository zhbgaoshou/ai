import { defineStore } from "pinia";
import themes from 'daisyui/src/theming/themes'

type Theme = keyof typeof themes;  // 确保 Theme 类型是 themes 的键

const themeInit = localStorage.getItem('theme') || 'light';
export const useSettingsStore = defineStore("settings", {
    state: () => {
        return {
            themes: ['light', 'dark', 'wireframe', 'lofi'],
            currentTheme: 'light',
        };
    },
    actions: {
        setTheme(themeName: string) {
            document.documentElement.setAttribute('data-theme', themeName);
            this.currentTheme = themeName;
            localStorage.setItem('theme', themeName);
        },
        getTheme() {
            // 将 themeName 显式转换为 Theme 类型
            const filteredThemes = this.themes.reduce((acc, themeName) => {
                if (themes[themeName as Theme]) {
                    acc[themeName] = themes[themeName as Theme];  // 强制将 themeName 作为 Theme 类型
                }
                return acc;
            }, {} as Record<string, Record<string, string>>);

            return filteredThemes;
        },
        initSettings() {
            this.setTheme(themeInit);
        }
    }
});