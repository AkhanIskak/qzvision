import {Injectable} from "@nestjs/common";
import {Repository} from "typeorm";
import {BusEntity} from "./bus.entity";
import {InjectRepository} from "@nestjs/typeorm";

@Injectable()
export class BusesService {
    constructor(
        @InjectRepository(BusEntity)
        private busesRepo: Repository<BusEntity>
    ) {
    }

    listBuses() {
        return this.busesRepo.find();
    }

}
