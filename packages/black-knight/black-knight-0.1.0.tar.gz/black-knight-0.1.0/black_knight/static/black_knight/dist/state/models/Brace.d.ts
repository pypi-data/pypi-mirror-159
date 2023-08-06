interface BraceInfoModel {
    preserve_filters: boolean;
    show_search: boolean;
    search_help_text: null | string;
    full_result_count: null | number;
    empty_value_display: string;
    actions: ActionModel[] | null;
    headers: string[];
    orders: string[];
}
interface BraceListModel {
    results: ResultModel[];
    ordered_by: string[];
}
interface ActionModel {
    name: string;
    description: string;
}
declare type PK = string | number;
declare type ResultModel = [PK, ...ResultRow[]];
declare type RImage = ['image', string | null];
declare type ResultRow = string | number | boolean | null | RImage;
declare type TLoading = ['loading', string];
declare type TPKMap = {
    [k: number]: PK;
};
export { BraceListModel, ActionModel, BraceInfoModel };
export { ResultModel, PK, ResultRow };
export { TLoading, TPKMap };
//# sourceMappingURL=Brace.d.ts.map