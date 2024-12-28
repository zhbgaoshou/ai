import { defineStore } from "pinia";
import { loginApi, infoApi, registerApi } from "@/api/user";
import { getModelsApi } from "@/api/chat";
import type { IAuthData, IInfo, IModel } from "@/types";
import { setRefreshToken, setToken, getToken, removeToken } from "@/utils/auth";

export const useUserStore = defineStore("user", {
  state: () => {
    return {
      token: getToken(),
      authData: {
        username: "萧炎",
        password: "xiaoyan",
      } as IAuthData,
      info: {} as IInfo,
      models: [] as IModel[],
      defaultModel: JSON.parse(localStorage.getItem("defaultModel") as string) || {}
    };
  },
  getters: {
    isLogin: (state) => state.token !== "",
    firstName: (state) => state.info.username?.split("")[0].toUpperCase(),
    userId: (state) => state.info.id,
    isSupperUser: (state) => state.info.is_superuser,
  },
  actions: {
    async register() {
      await registerApi(this.authData);
    },
    logout() {
      this.token = "";
      removeToken();
      location.reload();
    },
    async login() {
      const res = await loginApi(this.authData);
      this.token = res.access_token;
      setToken(res.access_token);
      setRefreshToken(res.refresh_token);
      await this.getInfo();
    },
    async getInfo() {
      const res = await infoApi();
      this.info = res;
      return res;
    },
    resetAuthData() {
      this.authData = {} as IAuthData;
    },
    async getModels() {
      this.models = await getModelsApi();
      if (!this.defaultModel.name) {
        const defaultModel = this.models.find((item) => item.default_model) || ({} as IModel)
        this.setDefaultModel(defaultModel)
      }
    },
    setDefaultModel(model: IModel) {
      if (model.is_vip && !this.isSupperUser) {
        // 如果 model 是 VIP 且用户不是超级用户，直接返回
        return;
      }

      // 如果通过校验，则设置默认模型并保存到本地存储
      this.defaultModel = model;
      localStorage.setItem("defaultModel", JSON.stringify(model));
    }

  },
});
