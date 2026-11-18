// Lets the email images (/email/*.jpg) be read by other sites, so they can be attached in Gmail.
export default async (request, context) => {
  const res = await context.next();
  const headers = new Headers(res.headers);
  headers.set("Access-Control-Allow-Origin", "*");
  return new Response(res.body, { status: res.status, headers });
};

export const config = { path: "/email/*" };
