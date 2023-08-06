interface ResponseOk {
    ok: true;
    data: any;
}
interface ResponseError {
    ok: false;
    message: string;
    code: number;
}
declare type Response = ResponseOk | ResponseError;
declare type TRequest = (url: string, method?: 'POST' | 'GET', signal?: AbortSignal, data?: Object) => Promise<Response>;
declare const REQUEST: TRequest;
export { REQUEST };
//# sourceMappingURL=request.d.ts.map