// Vercel Serverless Function 实现GitHub原始文件代理
export default async function handler(request, response) {
  try {
    // 从请求参数中获取路径
    let path = "/";
    if (request.query.path) {
      if (Array.isArray(request.query.path)) {
        path = "/" + request.query.path.join("/");
      } else {
        path = "/" + request.query.path;
      }
    }

    // 从查询参数中获取用户提供的token
    const userToken = request.query["nine-token"];

    // 从环境变量中获取预期的token（在Vercel中配置）
    const expectedToken = process.env.NINE49TOKEN;

    // 验证token是否匹配环境变量
    if (!userToken || userToken !== expectedToken) {
      // token不匹配或缺失时重定向到百度
      response.status(302).redirect("https://www.baidu.com");
      return;
    }

    // 检查路径是否为空或根路径
    if (path === "/" || path === "") {
      // 如果没有指定路径，重定向到百度
      response.status(302).redirect("https://www.baidu.com");
      return;
    }

    // 构造GitHub原始文件地址
    const githubRawUrl = `https://raw.githubusercontent.com${path}`;

    // 创建带认证的请求头
    const headers = {
      Authorization: `Bearer ${process.env.GITHUB49TOKEN}`, // 使用GitHub令牌认证
    };

    // 向GitHub发起请求
    const githubResponse = await fetch(githubRawUrl, { headers });

    // 检查响应状态码是否为成功状态
    if (!githubResponse.ok) {
      // 如果GitHub返回错误，重定向到百度
      response.status(302).redirect("https://www.baidu.com");
      return;
    }

    // 获取GitHub响应的内容和内容类型
    const content = await githubResponse.arrayBuffer();
    const contentType = githubResponse.headers.get("content-type");

    // 设置响应头并返回GitHub的响应内容
    response.setHeader(
      "Content-Type",
      contentType || "application/octet-stream"
    );
    response.status(200).send(Buffer.from(content));
  } catch (error) {
    // 捕获所有异常并重定向到百度
    response.status(302).redirect("https://www.baidu.com");
  }
}
