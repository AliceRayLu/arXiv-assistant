import axios, { AxiosRequestConfig } from "axios";

// 封装一下发起请求的部分, 便于本地测试时调用
function request(args: AxiosRequestConfig<any>) {
  args.baseURL = "http://localhost:8000";
  args.withCredentials = true;
  return axios.request(args);
}

export { request };
